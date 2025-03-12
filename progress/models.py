from django.db import models
from courses.models import Course
# Create your models here.
class Progress(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_lessons = models.IntegerField(default=0)
    total_lessons = models.IntegerField(default=1)  # Prevent division by zero
    progress_percentage = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.progress_percentage = (self.completed_lessons / self.total_lessons) * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.name} - {self.progress_percentage}%"
