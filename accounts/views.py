from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Account

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        address = data.get('address')
        
        if not password or len(password) > 20:
            return JsonResponse({'error': 'Password cannot be empty or longer than 20 characters.'}, status=400)
            
        if Account.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
            
        
        user = Account.objects.create(
            username=username, 
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            age=age,
            address=address
        )
        return JsonResponse({'message': 'User created successfully'}, status=201)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        try:
            user = Account.objects.get(username=username)
            if user.password == password:
                return JsonResponse({'message': 'Login successful!'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid password'}, status=400)
        except Account.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)