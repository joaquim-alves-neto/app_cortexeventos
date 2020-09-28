from django.db import models

# Create model COURSE

class Course(models.Model):

    # Create field of choices

    WITHOUT_CATEGORY = 'WC'
    ONLINE_COURSE = 'OC'
    GRADUATION_COURSE = 'GC'
    MENTORING_COURSE = 'MC'


    CATEGORIES = (
        (WITHOUT_CATEGORY, 'Sem categoria'),
        (ONLINE_COURSE, 'Curso online'),
        (GRADUATION_COURSE, 'Curso de formação'),
        (MENTORING_COURSE, 'Curso de mentoria'),
    )

    # Creation of fields

    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORIES, default=WITHOUT_CATEGORY)
    # image = models.ImageField(upload_to='media')

    # Class Meta

    class Meta:
        app_label = 'courses'