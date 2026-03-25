from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def blog(request):
    students_list = [
        {
            "name": "Rakshith",
            "class": "10th"
        },
        
        {
            "name": "Rohith",
            "class": "11th"
        },
        
        {
            "name": "Rakesh",
            "class": "12th"
        },
        
    ]
    return render(request, 'blog.html', {'students':students_list})