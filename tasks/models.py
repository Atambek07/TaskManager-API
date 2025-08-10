from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='tasks/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=50, verbose_name='name')

    def __str__(self):
        return self.title
