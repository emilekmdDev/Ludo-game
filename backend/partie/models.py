from django.db import models
from django.contrib.auth.models import User

COLOR_CHOICES = [
    ('r', 'red'),
    ('y', 'yellow'),
    ('b', 'blue'),
    ('g', 'green'),
    ('', ''),
]

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, blank=True)  # Par exemple 'red', 'blue', 'green', 'yellow'
    is_turn = models.BooleanField(default=False)  # Pour savoir si c'est au joueur de jouer
    
    def __str__(self):
        return self.user.username

class Room(models.Model):
    room_name = models.CharField(max_length=128, unique=True)
    members = models.ManyToManyField(Player, related_name='rooms', blank=True)  # Relier Room et Player via ManyToMany
    is_private = models.BooleanField(default=False)
    
    # Gestion des couleurs disponibles dans la room
    red_taken = models.BooleanField(default=False)
    blue_taken = models.BooleanField(default=False)
    green_taken = models.BooleanField(default=False)
    yellow_taken = models.BooleanField(default=False)
    
    def __str__(self):
        return self.room_name
    
    def available_colors(self):
        colors=[]
        
        if not self.red_taken:
            colors.append({'color':'r', 'taked':self.red_taken})
        
        if not self.blue_taken:
            colors.append({'color':'b', 'taked':self.blue_taken})
        
        if not self.yellow_taken:
            colors.append({'color':'y', 'taked':self.yellow_taken})
        
        if not self.green_taken:
            colors.append({'color':'g', 'taked':self.green_taken})
        
        return colors
    def assign_color(self, player, color):
        """Assigne une couleur à un joueur si elle est disponible et non attribuée."""
        if player.color:  # Le joueur a déjà une couleur, on la libère d'abord
            self.release_color(player)

        if color == 'r' and not self.red_taken:
            self.red_taken = True
            player.color = 'r'
        elif color == 'b' and not self.blue_taken:
            self.blue_taken = True
            player.color = 'b'
        elif color == 'g' and not self.green_taken:
            self.green_taken = True
            player.color = 'g'
        elif color == 'y' and not self.yellow_taken:
            self.yellow_taken = True
            player.color = 'y'
        else:
            raise ValueError("La couleur est déjà prise ou invalide")

        player.save()
        self.save()

    def release_color(self, player):
        colors = ['r','b','y','g'] 

        for color in colors:
            if player.color == color:
                if color == 'r':
                    self.red_taken=False
                elif color == 'g':
                    self.green_taken_taken=False
                elif color == 'b':
                    self.blue_taken_taken=False
                elif color == 'y':
                    self.yellow_taken_taken=False
        player.color=''
        
        player.save()
        self.save()

    def update_colors_set(self):
        """Met à jour l'état des couleurs prises en fonction des joueurs dans la salle."""
        self.red_taken = self.members.filter(color='r').exists()
        self.blue_taken = self.members.filter(color='b').exists()
        self.green_taken = self.members.filter(color='g').exists()
        self.yellow_taken = self.members.filter(color='y').exists()
        self.save()
