from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Recipe

def home(request):
    return render(request, 'home.html')

def recipes(request):
    return render(request, 'recipes.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return redirect('thank_you')
    return render(request, 'contact.html')

def thank_you(request):
    return render(request, 'thankyou.html')

def submit_contact(request):
    if request.method == 'POST':
        return redirect('thank_you')
    return render(request, 'contact.html')

# Add this signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Automatically log in the user
            return redirect('home')  # Redirect to home or another page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
