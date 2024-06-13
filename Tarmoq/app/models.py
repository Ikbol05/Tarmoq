from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class Friend(models.Model):
    user_dan = models.ForeignKey(User, related_name='user_dan', on_delete=models.CASCADE)
    user_ga = models.ForeignKey(User, related_name='user_ga', on_delete=models.CASCADE)

class Message(models.Model):
    user1 = models.ForeignKey(User, related_name='user_1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user_2', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)