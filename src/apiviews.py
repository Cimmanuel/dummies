from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all().exclude(is_superuser=True)
	serializer_class = UserSerializer
	
