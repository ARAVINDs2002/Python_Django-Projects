from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

def home(request):
    """Simple landing page"""
    return render(request, 'profiles/home.html')

def profile_view(request):
    """
    Realistic profile view where user can add/edit their profile info.
    For this demo, we'll use a fixed user or the first one if not logged in.
    """
    # Just for demo simplicity, we'll auto-create/get the first user's profile
    # If using auth properly, this would be request.user
    user, created = User.objects.get_or_create(username='demo_user')
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profiles/profile.html', {
        'profile': profile,
        'form': form
    })
