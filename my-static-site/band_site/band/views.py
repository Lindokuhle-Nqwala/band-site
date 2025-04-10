from django.shortcuts import render, redirect
from .models import BandMember, Concert
from .forms import RegisterForm

def home(request):
    """
    Display the home page of the band site.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered home page.
    """
    return render(request, 'band/home.html')

def band_members(request):
    """
    Retrieve and display a list of all band members.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template showing band members.
    """
    members = BandMember.objects.all()
    context = {'members': members}
    return render(request, 'band/band_members.html', context)

def concerts(request):
    """
    Retrieve and display upcoming concerts.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template showing concert details.
    """
    shows = Concert.objects.all()
    context = {'concerts': shows}
    return render(request, 'band/concerts.html', context)

def register(request):
    """
    Process user registration using the RegisterForm.

    For GET requests, the function shows the blank registration form.
    For POST requests, it validates and saves the form, and then redirects
    the user to the login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template for registration or redirection on success.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'band/register.html', context)
