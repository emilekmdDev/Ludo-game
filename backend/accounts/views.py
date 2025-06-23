# views.py
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from partie.models import Player

@csrf_exempt  # À utiliser avec précaution (pour les tests), mieux vaut configurer CSRF correctement.
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if request.user.is_authenticated:
            user_data = {
                'id': request.user.id,
                'username': request.user.username,
            }
            
            return JsonResponse({
                'message': 'Already logged in',
                'status': 'success',
                'user': user_data
            }, status=200)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            user_data = {
                'id': user.id,
                'username': user.username,
                # 'email': user.email
            }
            login(request, user)
            return JsonResponse({
                'message': 'Login successful', 
                'status': 'success',
                'user':user_data
                }, status=200)
        else:
            return JsonResponse({'message': 'Invalid credentials', 'status': 'error'}, status=400)
        
    return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse(
            {
                'message': 'Logout successful', 
                'status': 'success'
            }, status=200)
        
    return JsonResponse(
        {
            'message': 
            'Method not allowed'
        }, status=405)
    
@csrf_exempt
def sign_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message':'user name already exists', 'status':'error'}, status=400)
        
        user_data = {
                'id': request.user.id,
                'username': request.user.username,
            }
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        Player.objects.get_or_create(user=user)
        login(request, user)
        user_data = {
                'id': request.user.id,
                'username': request.user.username,
            }
        
        return JsonResponse({'message':'User created successfully', 'user':user_data},status=201)
    
    return JsonResponse({'message':'Method not allowed'}, status=405)