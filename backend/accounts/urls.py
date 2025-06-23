from django.urls import path
from .views import *

urlpatterns = [
    path('api/login/', login_view, name='login'),
    path('api/logout/', logout_view, name='logout'),
    path('api/sign-in/', sign_view, name='sign-in'),
]
