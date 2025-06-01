from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('mentor', 'Mentor'),
        ('mentee', 'Mentee'),
        ('both', 'Both'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    skills = models.TextField()
    goals = models.TextField()
    availability = models.TextField()

class Review(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Resource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)