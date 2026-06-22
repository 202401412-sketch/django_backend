from django.contrib import admin
from django.urls import path
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        return Response({'message': 'Login Successful', 'status': 'success'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid Username or Password', 'status': 'fail'}, status=status.HTTP_400_BAD_REQUEST)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/login/', login_api),    
]