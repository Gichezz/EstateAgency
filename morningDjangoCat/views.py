from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


def indx(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def agent_single(request):
    return render(request, 'agent-single.html')


def contact(request):
    return render(request, 'contact.html')


def agents_grid(request):
    return render(request, 'agents-grid.html')


def blog_grid(request):
    return render(request, 'blog-grid.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def property_grid(request):
    return render(request, 'property-grid.html')


def property_single(request):
    return render(request, 'property-single.html')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('users-registration')
        else:
            messages.error(request, 'Account creation failed')
            return redirect('users-registration')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
