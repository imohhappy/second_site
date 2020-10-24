from django.db import models


MARRIAGE = (('SG', 'single'), ('MD', 'married'), ('DV', 'divorced'), ('FR', 'freed'))
GENDER = (('CH',  'choose...'), ('M', 'male'), ('F', 'female'))
RELATIONSHIP = (('B', 'brother'), ('S', 'sister'), ('F', 'father'), ('M', 'mother'))


class Marriage(models.Model):
    passport = models.ImageField(upload_to='pics')
    surname = models.CharField(max_length=20, default='surname')
    first_name = models.CharField(max_length=20, default='first name')
    other_names = models.CharField(max_length=20, default='other names')
    gender = models.CharField(max_length=30, choices=GENDER, default='choose...')
    phone_number = models.IntegerField()
    phone_number_2 = models.IntegerField()
    marital_status = models.CharField(max_length=20, choices=MARRIAGE)
    date_of_birth = models.DateField(default='mnt/day/yr')
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    gender_2 = models.CharField(max_length=20, choices=GENDER, default='choose...')
    relationship = models.CharField(max_length=20, choices=RELATIONSHIP, default='choose...')

# Create your models here.
