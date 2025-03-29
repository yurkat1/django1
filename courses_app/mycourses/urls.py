from django.urls import path
from mycourses.views import my_page

urlpatterns = [
    path("", my_page, name="courses_page"),
]