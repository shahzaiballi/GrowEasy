from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Review, Goal, Post, Resource
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_type', 'skills', 'goals', 'availability', 'photo']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES)
    skills = forms.CharField(widget=forms.Textarea)
    goals = forms.CharField(widget=forms.Textarea)
    availability = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 'skills', 'goals', 'availability', 'photo']

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
    niche = request.GET.get('niche', '').lower()
    mentors = Profile.objects.filter(user_type__in=['mentor', 'both'])
    mentees = Profile.objects.filter(user_type__in=['mentee', 'both'])
    if niche and niche != 'more':
        mentors = mentors.filter(skills__icontains=niche)
        mentees = mentees.filter(goals__icontains=niche)
    context = {
        'mentors': mentors,
        'mentees': mentees,
        'niche': niche if niche != 'more' else None,
    }
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = Profile(
                user=user,
                user_type=form.cleaned_data['user_type'],
                skills=form.cleaned_data['skills'],
                goals=form.cleaned_data['goals'],
                availability=form.cleaned_data['availability'],
                photo=form.cleaned_data['photo']
            )
            profile.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    
    # Add mentors and mentees to the context, similar to index view
    niche = request.GET.get('niche', '').lower()
    mentors = Profile.objects.filter(user_type__in=['mentor', 'both'])
    mentees = Profile.objects.filter(user_type__in=['mentee', 'both'])
    if niche and niche != 'more':
        mentors = mentors.filter(skills__icontains=niche)
        mentees = mentees.filter(goals__icontains=niche)
    
    context = {
        'form': form,
        'profile': profile,
        'mentors': mentors,
        'mentees': mentees,
        'niche': niche if niche != 'more' else None,
    }
    return render(request, 'profile.html', context)

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
            mentor = User.objects.filter(profile__user_type__in=['mentor', 'both']).first()
            review.mentor = mentor
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    reviews = Review.objects.filter(mentor__profile__user_type__in=['mentor', 'both'])
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

@login_required
def pro(request):
    return render(request, 'pro.html')