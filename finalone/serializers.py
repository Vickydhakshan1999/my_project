from rest_framework import serializers
from .models import User  # Adjust this import based on your User model location

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone_number', 'role', 'custom_fields']


def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Flatten the custom fields
        custom_fields = representation.pop('custom_fields', {})
        representation.update(custom_fields)
        
        return representation