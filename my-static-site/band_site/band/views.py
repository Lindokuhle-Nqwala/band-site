from django.shortcuts import render
from .models import Concert
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



# Create your views here.
def home(request):
    return render(request, 'band/home.html')

def concerts(request):
    concerts = Concert.objects.all()
    return render(request, 'band/concerts.html', {'concerts': concerts})

def band_members(request):
    return render(request, 'band/band_members.html')


@login_required
def concerts(request):
    concerts = Concert.objects.all()
    return render(request, 'band/concerts.html', {'concerts': concerts})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to homepage after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'band/register.html', {'form': form})
