from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import Admin  # Import your custom Admin model

def Home(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index1.html')

from django.contrib.auth.hashers import make_password

def SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        role = request.POST.get('role')
        admin_code = request.POST.get('admin-code', '').strip()

        print(f"Username: {uname}, Email: {email}, Role: {role}, Admin code: {admin_code}")  # Debug output

        if role == 'admin':
            if admin_code != '1234':  # Replace '1234' with your actual admin code logic
                return render(request, 'signup.html', {
                    'error_message': 'Invalid admin code. Please try again.'
                })

            # Create an entry in the Admin table
            try:
                admin_user = Admin.objects.create(
                    username=uname,
                    email=email,
                    password=make_password(pass1),  # Securely hash the password
                    admin_code=admin_code
                )
                admin_user.save()
            except Exception as e:
                return render(request, 'signup.html', {
                    'error_message': 'Failed to create admin user. Please try again.'
                })
        else:
            # Create a regular user
            try:
                my_user = User.objects.create_user(username=uname, email=email, password=pass1)
                my_user.save()
            except Exception as e:
                return render(request, 'signup.html', {
                    'error_message': 'Failed to create user. Please try again.'
                })

        return redirect('home')

    return render(request, 'signup.html', {})
from django.contrib.auth.hashers import check_password

from django.contrib.auth.hashers import check_password

def LogIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get the email
        pass1 = request.POST.get('password')  # Get the password
        role = request.POST.get('role')  # Get the role (user/admin)
        admin_code = request.POST.get('admin-code', '').strip()  # Get admin code, if provided

        if role == 'admin':
            # Admin login
            try:
                admin_user = Admin.objects.get(email=email)  # Retrieve the admin by email
                if check_password(pass1, admin_user.password) and admin_user.admin_code == admin_code:
                    # Set session manually for admin
                    request.session['admin_user'] = admin_user.username
                    return redirect('home')
                else:
                    return HttpResponse("Invalid admin credentials. Please try again.")
            except Admin.DoesNotExist:
                return HttpResponse("Admin with this email does not exist.")
        else:
            # Regular user login
            try:
                user = User.objects.get(email=email)  # Retrieve the user by email
                user = authenticate(request, username=user.username, password=pass1)  # Authenticate user
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse("Email or Password is incorrect!")
            except User.DoesNotExist:
                return HttpResponse("User with this email does not exist.")

    return render(request, 'login.html')



def LogOut(request):
    logout(request)  # Properly log out the user
    return redirect('Home')  # Redirect to the Home page
