from rest_framework import serializers
from main.models import *

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
