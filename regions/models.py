from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class regiao (models.Model):
    id_regiao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_regiao = models.CharField(max_length=25)
    create_at = models.DateField(auto_now_add=True)

class fruta (models.Model):
    id_fruta = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_fruta = models.CharField(max_length=100)
    id_regiao = models.ForeignKey(regiao, on_delete=models.PROTECT)