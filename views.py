from django.shortcuts import render
from courses.forms import CourseForm

# Create view REGISTER_COURSE

def register_course(request):
    form = CourseForm()
    return render(request, 'register_course.html', {'form':form})