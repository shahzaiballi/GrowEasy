from django.contrib import admin
from django.urls import path, include
from mentorship import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Removed duplicate admin entry
    path('', views.index, name='index'),
    path('profiles/', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('schedule/', views.schedule, name='schedule'),
    path('chat/', views.chat, name='chat'),
    path('reviews/', views.reviews, name='reviews'),
    path('progress/', views.progress, name='progress'),
    path('community/', views.community, name='community'),
    path('resources/', views.resources, name='resources'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('pro/', views.pro, name='pro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)