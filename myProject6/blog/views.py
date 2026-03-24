from django.shortcuts import render

from datetime import datetime

def blog_details(request): 
    post = {
        "title": "My second Template Post",
        "description": "Django is a high-level python web framework that workks in backend",
        "author": None,
        "created_at": datetime(2026,3,24,9,34),
        "comments_count": 5,
        "tags": ["Django", "Python", "Web Development"],
        "price": 100,
        "number": 7,
    }
    return render(request, 'blog/blog_details.html', {"post": post})
