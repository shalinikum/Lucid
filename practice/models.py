from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    clinic = models.CharField(max_length=50)
    consultation_fee = models.IntegerField(default=500)
    email = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    therapist = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    joining_date = models.DateTimeField('date published')

class Appointment(models.Model):
    therapist = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting_time = models.DateTimeField('your slot')
    feedback  = models.CharField(max_length=500)

class WordsAttribute(models.Model):
    phoneme = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    illustration_video = models.CharField(max_length=50)

class Word(models.Model):
    word = models.CharField(max_length=50)
    image = models.CharField(max_length=500) 
    audio_file = models.CharField(max_length=500)
    illustration_video = models.CharField(max_length=50)
    attribute = models.ForeignKey(WordsAttribute, on_delete=models.CASCADE)

class UserRecording(models.Model):
    recorded_audio = models.CharField(max_length=50)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    word =   models.ForeignKey(Word, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')

class UserTask(models.Model):
    task = models.ForeignKey(WordsAttribute, on_delete=models.CASCADE)
    count = models.IntegerField(default=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
