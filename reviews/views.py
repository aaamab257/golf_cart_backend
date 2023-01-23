from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .serialirzer import *
from users.renderers import UserRenderer
# Create your views here.


class MakeReview(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self , request , format=None):
        user = request.user
        serializer = ReviewSerializer(context = {'user':user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Your review sent successfully', 'data' : serializer.data})
