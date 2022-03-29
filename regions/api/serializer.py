from rest_framework import serializers
from regions import models

class regionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.regiao
        fields = '__all__'

class fruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.fruta
        fields = '__all__'