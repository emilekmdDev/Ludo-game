from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/ludo/<str:room_name>/<str:action>/', consumers.LudoConsumer.as_asgi()),
]