from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/", views.courses, name="courses"),
    path("ft-courses/", views.ft_courses, name="ft-courses"),
    path("aboutus/", views.about_us, name="about-us"),
    path("courses/BCA", views.bca_course, name="bca_course"),
    path("courses/BBA", views.bba_course, name="bba_course"),
    path("courses/MCA", views.mca_course, name="mca_course"),
]