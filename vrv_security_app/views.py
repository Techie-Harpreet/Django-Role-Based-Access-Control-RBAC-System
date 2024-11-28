from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    
    if user.is_superuser:
        # Admin Dashboard
        context = {
            'dashboard_title': 'Admin Dashboard',
            'welcome_message': 'Welcome to the Admin Dashboard',
            'permissions': ['Manage Users', 'View Reports', 'Access All Data'],
        }
        return render(request, 'dashboard/admin_dashboard.html', context)

    elif user.is_staff:
        # Moderator Dashboard
        context = {
            'dashboard_title': 'Moderator Dashboard',
            'welcome_message': 'Welcome to the Moderator Dashboard',
            'permissions': ['Moderate Content', 'Manage User Reports', 'View Analytics'],
        }
        return render(request, 'dashboard/moderator_dashboard.html', context)

    else:
        # User Dashboard
        context = {
            'dashboard_title': 'User Dashboard',
            'welcome_message': 'Welcome to your Dashboard',
            'permissions': ['View Profile', 'Update Information', 'Access Personalized Content'],
        }
        return render(request, 'dashboard/user_dashboard.html', context)
    
def RegisterUser(request):
    if request.method == "POST":
        # Get data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')  # password1 from the form
        password_confirm = request.POST.get('password2')  # password2 from the form
        role = request.POST.get('role')  # Role selected during registration (User, Moderator, Admin)
        
        # Check if passwords match
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Assign group based on the role
        if role == 'Admin':
            user.is_staff = True  # Admins need staff privileges
            user.is_superuser = True  # Admins are superusers
            user.save()
            messages.success(request, "Admin registration successful!")
        elif role == 'Moderator':
            user.is_staff = True  # Moderators are staff but not superusers
            user.save()
            messages.success(request, "Moderator registration successful!")
        else:  # Default to User
            messages.success(request, "User registration successful!")
        
        return redirect('login')  # Redirect to login page after successful registration


    return render(request, "pages/register.html")

def user_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # Check if the input is an email or username
        user = None
        if '@' in username_or_email:  # If the input is an email
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                user = None
        else:  # If the input is a username
            user = User.objects.filter(username=username_or_email).first()

        if user is not None:
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                return redirect('home')  # Replace 'home' with your desired route
            else:
                messages.error(request, "Invalid password. Please try again.")
        else:
            messages.error(request, "User with this email/username does not exist.")
    
    return render(request, 'pages/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout