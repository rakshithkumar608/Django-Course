from django.shortcuts import render

from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def home(request):
    context = {
        "name": "Rakshith",
        "age": 25,
        "skills": ["Python", "Js", "React"],
        "user":User("Gowda",20),
        "blog": {
            "title": "Django Template Intro",
            "author":{
                "name": "Rakshith Gowda"
            },
            "content": "<b>This is bold</b>",
            "created_at": datetime(2026,3,24,8,7)
        },
        "empty_value": None,
    }
    return render(request, "blog/home.html",context)
