from django.contrib import admin  # type: ignore

# Register your models here.
from posts.models import Post



admin.site.register(Post)