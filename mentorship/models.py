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
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)  # Changed to ImageField

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Review(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentees')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Resource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)