from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('schedule/', views.schedule, name='schedule'),
    path('chat/', views.chat, name='chat'),
    path('reviews/', views.reviews, name='reviews'),
    path('progress/', views.progress, name='progress'),
    path('community/', views.community, name='community'),
    path('resources/', views.resources, name='resources'),
    path('signup/', views.signup, name='signup'),
]