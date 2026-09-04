from django.db import models  # type: ignore[reportMissingModuleSource]

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)

