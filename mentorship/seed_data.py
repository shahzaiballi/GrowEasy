import os
import sys
import django

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groweasy.settings')
django.setup()

from django.contrib.auth.models import User
from mentorship.models import Profile

def create_dummy_data():
    # Create Mentors
    mentor1 = User.objects.create_user(username='john_mentor', password='pass123', email='john@example.com')
    mentor1_profile = Profile.objects.create(
        user=mentor1,
        user_type='mentor',
        skills='Python, Django, Career Coaching',
        goals='Help mentees grow in tech',
        availability='Weekdays 9 AM - 12 PM',
        photo='https://images.unsplash.com/photo-1500648767791-00dcc994a43e'
    )

    mentor2 = User.objects.create_user(username='sarah_mentor', password='pass123', email='sarah@example.com')
    mentor2_profile = Profile.objects.create(
        user=mentor2,
        user_type='mentor',
        skills='JavaScript, React, Leadership',
        goals='Guide mentees in frontend development',
        availability='Weekends 2 PM - 5 PM',
        photo='https://images.unsplash.com/photo-1494790108377-be9c29b29330'
    )

    # Create Mentees
    mentee1 = User.objects.create_user(username='alice_mentee', password='pass123', email='alice@example.com')
    mentee1_profile = Profile.objects.create(
        user=mentee1,
        user_type='mentee',
        skills='Beginner Python, HTML',
        goals='Learn backend development',
        availability='Evenings 6 PM - 8 PM',
        photo='https://images.unsplash.com/photo-1517841903200-7b8d4b4a4f4c'
    )

    mentee2 = User.objects.create_user(username='bob_mentee', password='pass123', email='bob@example.com')
    mentee2_profile = Profile.objects.create(
        user=mentee2,
        user_type='mentee',
        skills='JavaScript, CSS',
        goals='Master React and get a job',
        availability='Mornings 10 AM - 12 PM',
        photo='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d'
    )

    # Create Both
    both1 = User.objects.create_user(username='emma_both', password='pass123', email='emma@example.com')
    both1_profile = Profile.objects.create(
        user=both1,
        user_type='both',
        skills='Django, Data Science, Mentoring',
        goals='Learn AI and mentor others',
        availability='Weekdays 3 PM - 5 PM',
        photo='https://images.unsplash.com/photo-1529626455594-4ff0802cfb3a'
    )

if __name__ == "__main__":
    try:
        create_dummy_data()
        print("Dummy data created successfully!")
    except Exception as e:
        print(f"Error creating dummy data: {e}")