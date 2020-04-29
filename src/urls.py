from django.urls import path
from .apiviews import UserList

urlpatterns = [
	path('users/', UserList.as_view(), name='users'),
]
