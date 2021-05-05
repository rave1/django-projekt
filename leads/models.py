from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
## Tabela w bazie w postaci klasy, models.Someth jest wbudowane w django


class User(AbstractUser): #dziedzicze z wbudowanego modelu uzytkownika w django
    pass

class Lead(models.Model):
'''
    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google','Google'),
        ('Newsletter', 'Newsletter'),
    )
'''
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent" on_delete=models.CASCADE) # przy usunieciu agenta, Lead tez sie usuwa


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # OneToOne -> kazdy agent ma jednego uzytkownika


       

'''
    phoned = models.BooleanField(default=False)
    source  = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    profile_picture = models.ImageField(blank=True, null=True) ##blank -> pusty string
    special_files = models.FileField(blank=True, null=True)
'''