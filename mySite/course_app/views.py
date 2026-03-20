from django.shortcuts import render

def course_list(request):
    return render(request, 'course_app/course_list.html')


def course_detail(request):
    return render(request, 'course_app/course_detail.html')