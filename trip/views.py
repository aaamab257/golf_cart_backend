from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from users.renderers import UserRenderer
# Create your views here.


class MakeTrip(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self , request , format=None):
        student = request.user
        serializer = TripSerializer(context = {'student':student})
        if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response({'msg':'Your request sent successfully', 'data' : serializer.data})