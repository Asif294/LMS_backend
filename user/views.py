from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import User 
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializers
@api_view(['GET','POST'])
def user_list_create(request):
    if request.method=='GET':
        if not request.user.is_authenticated:
            return Response({'details':'Authentication crediantial are not provided'},status=401)
        if request.user.role=='admin':
            user=User.objects.all()
        else:
            user=User.objects.filter(id=request.user.id)
        serializer =UserSerializers(user,many=True)
        return Response (serializer.data)
    elif request.method=='POST':
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    