from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking
from .serializers import bookingSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your views here.
def home(request):
    return render(request, 'index.html')

class bookingview(APIView):
    
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','groups']
        
