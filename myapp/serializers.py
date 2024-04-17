
from rest_framework import serializers
from .models import UserRegistration

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'
