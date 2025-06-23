from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from .models import Room,Player
import random

class LudoConsumer(WebsocketConsumer):
    def connect(self):
        
        # Vérifier si l'utilisateur est authentifié avant de continuer
        if self.scope['user'].is_authenticated:
            self.user = self.scope['user']  # Utilisateur authentifié
            self.player, _ = Player.objects.get_or_create(user=self.user)  # Créer ou récupérer le Player
        else:
            self.close()  # Fermer la connexion si l'utilisateur n'est pas authentifié
            return
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.action = self.scope['url_route']['kwargs']['action']
        self.room_group_name = f'ludo_{self.room_name}'
        self.playroom=None
        
        # cas de creation
        if self.action=='create':
            # Joindre la room
            self.playroom, _ = Room.objects.get_or_create(room_name=self.room_name)
            
            colors=self.playroom.available_colors()
            if colors:
                self.playroom.assign_color(player=self.player,color=colors[0]['color'])
            
            if self.player not in self.playroom.members.all() and self.playroom.members.count()-1 <4:
                async_to_sync(self.channel_layer.group_add)(self.room_group_name,self.channel_name)
                self.playroom.members.add(self.player)
                self.update_game()
            self.accept()
        else:
            print('....................................here')
            self.playroom = Room.objects.get(room_name=self.room_name)
            
            if self.playroom:
            
                if self.player not in self.playroom.members.all() and self.playroom.members.count()-1 <4:
                    
                    colors=self.playroom.available_colors()
            
                    if colors:
                        self.playroom.assign_color(player=self.player,color=colors[0]['color'])
                        
                    async_to_sync(self.channel_layer.group_add)(self.room_group_name,self.channel_name)
                    
                    self.playroom.members.add(self.player)
                    self.update_game()
                self.accept()
                    
        print('/////////////////////////////////connexion etablie')

    def disconnect(self, close_code):
        # Quitter la room
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
        # Enlever l'utilisateur de la room
        if  self.player in self.playroom.members.all():
            self.playroom.release_color(player=self.player)
            self.playroom.members.remove(self.player)
            self.update_game()
        
        print('/////////////////////////////////connexion rompue')
        self.close()

    def receive(self, text_data):
        data = json.loads(text_data)
        
        action = data.get('action', None)  # Retourne None si 'action' n'est pas présent
        if action == 'leave':
            self.leave_room()
        
        # gestion et mise a jour du changement de couleur
        if action == 'changecolor':
            playername=data.get('playername', None)
            
            self.playroom.update_colors_set()
            colors=self.playroom.available_colors()

            if colors:
                for player in self.playroom.members.all():
                    if player.user.username==playername:
                        # self.playroom.release_color(player=player)
                        player.color=colors[int(random.random()*len(colors))]['color']
                        self.playroom.update_colors_set()
                        player.save()
                        
                        break
            else:
                self.send_message('pas de couleur dispo')
        
        if action == 'startparty':
            roomname=data.get('roomname',None)
            
            
        print('/////////////////////////////////paquet recu')
        self.update_game()
    
    def leave_room(self):        
        self.disconnect('')

    def update_game(self):
        online_count = self.playroom.members.count()
        room=Room.objects.get(room_name=self.room_name)
        
        users=[]
        if room:
            for player in room.members.all():
                users.append({'username': player.user.username, 'color': player.color})
        
        event = {
                'type': 'update',
                'message': {
                    'online_count': online_count,
                    'users':users
                }
            }
        # Diffuser la mise à jour du nombre de membres
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, event
        )
    
    def send_message(self,message_to_send):
        event = {
                'type': 'update',
                'message': {
                    'text':message_to_send,
                }
            }
        # Diffuser la mise à jour du nombre de membres
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, event
        )
        

    def update(self, event):
        message = event['message']  

        # Envoyer le message à WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))