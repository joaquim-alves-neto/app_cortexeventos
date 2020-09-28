# Import django forms/ModelForm

from django.forms import ModelForm
from courses.models import Course

# Create Form Course

class CourseForm(ModelForm):
    class Meta:
        model = Course;
        fields = ['title', 'description', 'category']