from django.shortcuts import render
from main.models import *
from main.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


api_view(['POST'])
def create_file(request):
    data = request.data
    serializer = FileSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    