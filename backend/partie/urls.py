from django.urls import path
from .views import *

urlpatterns = [
    path('api/create_room/', create_room, name='create_room'),
]
