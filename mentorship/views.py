from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Review, Goal, Post, Resource
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_type', 'skills', 'goals', 'availability']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['description']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'link']

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            if profile.pk:  # If profile exists, update it
                profile.save()
            else:  # If profile doesn't exist, create it
                profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form, 'profile': profile})

@login_required
def schedule(request):
    return render(request, 'schedule.html')

@login_required
def chat(request):
    return render(request, 'chat.html')

@login_required
def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.mentee = request.user
            review.mentor = request.user  # Replace with actual mentor selection logic
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    reviews = Review.objects.filter(mentor=request.user)
    return render(request, 'reviews.html', {'form': form, 'reviews': reviews})

@login_required
def progress(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('progress')
    else:
        form = GoalForm()
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'progress.html', {'form': form, 'goals': goals})

@login_required
def community(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('community')
    else:
        form = PostForm()
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community.html', {'form': form, 'posts': posts})

@login_required
def resources(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.user = request.user
            resource.save()
            return redirect('resources')
    else:
        form = ResourceForm()
    resources = Resource.objects.all().order_by('-created_at')
    return render(request, 'resources.html', {'form': form, 'resources': resources})