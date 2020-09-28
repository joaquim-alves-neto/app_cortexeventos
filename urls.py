from django.urls import path
from courses import views

app_name = 'courses'

urlpatterns = [
    path('register_course', views.register_course, name='register_course'),
]
