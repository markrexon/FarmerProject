from django.contrib import admin

from blogpost.models import BlogPost, Profile

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Profile)
