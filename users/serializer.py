from dataclasses import field
from rest_framework import serializers
from .models import User

class DRFUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"