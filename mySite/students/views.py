from django.shortcuts import render


def home(request):
    return render(request, 'students/home.html');

def about(request):
    return render(request, 'students/about.html')