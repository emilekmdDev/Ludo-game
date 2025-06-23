from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_room(request):    
    data = json.loads(request.body)
    room_name = data.get('roomname')
    is_private = data.get('private_')
    
    if request.method == 'POST':
        room,_=Room.objects.get_or_create(room_name=room_name,is_private=bool(is_private))
    
    # print(request.user.password)
    # print(request.user.username)    
    return JsonResponse({
                'status': 'success',
                'room_name': room_name 
            }, status=200)
    
    #     # user=User.objects.get(username=request.user.username)
    #     # room.user_online.add(user,request.user)
        
@csrf_exempt    
def join(request, username):    
    pass