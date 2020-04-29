from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(required=True)
	last_name = serializers.CharField(required=True)
	email = serializers.CharField(required=True, label='Email', validators=[UniqueValidator(queryset=User.objects.all())])
	
	password = serializers.CharField(
		write_only = True, style = {
			'input_type': 'password'
		}
	)

	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance

	def update(self, instance, validated_data):
		for attr, value in validated_data.items():
			if attr == 'password':
				instance.set_password(value)
			else:
				setattr(instance, attr, value)
		instance.save()
		return instance
