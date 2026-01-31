from django.shortcuts import render

def home(request):
    print("DEBUG: Home page accessed")
    return render(request, "home.html")