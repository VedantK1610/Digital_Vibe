from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from DEV.settings import EMAIL_HOST_USER

def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        course_select=request.POST.get('course-select')
        message=request.POST.get('message')

        data ={
            'name':name,
            'email':email,
            'course_select':course_select,
            'message':message
        }
        all_message='''
            For Course :{}

            From : {}

            Enquiry : {}
        '''.format(data['course_select'],data['email'],data['message'])

        send_mail(data['course_select'],all_message,EMAIL_HOST_USER,[data['email']],fail_silently=False,)
    return render(request,"index.html")

def courses(request):
    return render(request,"courses.html")

def contact_email(request):
    pass

def ft_courses(request):
    return render(request,"fameux-courses.html")