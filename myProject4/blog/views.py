from django.shortcuts import render

def post_list(request):
    return render(render, 'blog/post_list.html')
