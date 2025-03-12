from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Course(models.Model):
    PLATFORM_CHOICES = [
        ('Coursera', 'Coursera'),
        ('Udemy', 'Udemy'),
        ('Simplilearn', 'Simplilearn'),
        ('Udacity', 'Udacity'),
        ('edX', 'edX'),
        ('Pluralsight', 'Pluralsight'),
        ('LinkedIn Learning', 'LinkedIn Learning'),
        ('FutureLearn', 'FutureLearn'),
        ('Skillshare', 'Skillshare'),
        ('Khan Academy', 'Khan Academy'),
        ('Codecademy', 'Codecademy'),
        ('DataCamp', 'DataCamp'),
        ('Treehouse', 'Treehouse'),
        ('Forage', 'Forage'),
        ('IBM Skillsbuild', 'IBM Skillsbuild'),
        ('Udemycourses', 'Udemycourses'),
        ('Alison', 'Alison'),
        ('BitDegree', 'BitDegree'),
        ('OpenLearn', 'OpenLearn'),
        ('Stanford Online', 'Stanford Online'),
        ('Harvard Online', 'Harvard Online'),
        ('MIT OpenCourseWare', 'MIT OpenCourseWare'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=100, choices=PLATFORM_CHOICES)
    duration = models.IntegerField()  # Course duration in hours
    deadline = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
