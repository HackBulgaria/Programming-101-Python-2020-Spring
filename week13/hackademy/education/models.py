from django.db import models
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'Course "{self.name}"'

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date
