from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")

def courses(request):
    return render(request,"courses.html")

def ft_courses(request):
    return render(request,"fameux-courses.html")