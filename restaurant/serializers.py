from rest_framework import serializers
from .models import Menu

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        models = Menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        