from rest_framework import viewsets
from regions.api import serializer
from regions import models

class regionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.regionsSerializer
    queryset = models.regiao.objects.all()

class fruitViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.fruitsSerializer
    queryset = models.fruta.objects.all()
