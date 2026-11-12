from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def planner_page(request):
    return render(request, 'planner.html')

def profile_page(request):
    return render(request, 'profile.html')
