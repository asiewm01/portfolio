from django.shortcuts import render
from .models import Project, Skill

def home(request):
    return render(request, 'home.html')  # Make sure this template exists

def about_me(request):
    return render(request, 'about_me.html')  

def portfolio(request):
    return render(request, 'portfolio.html')  

def blog(request):
    return render(request, 'blog.html')  

def contact_me(request):
    return render(request, 'contact_me.html')  

def resume(request):
    return render(request, 'resume.html')  

def skills(request):
    return render(request, 'skills.html')  

def privacy_policy(request):
    return render(request, 'privacy_policy.html')  

def tech_stack(request):
    return render(request, 'tech_stack.html')  


