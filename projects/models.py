from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to="img/")