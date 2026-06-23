from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import MyUser

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if MyUser.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
            
        user = MyUser.objects.create(username=username, password=password)
        return JsonResponse({'message': 'User created successfully'}, status=201)