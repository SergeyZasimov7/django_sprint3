from django.contrib import admin

from .models import Category, Location, Post

admin.site.register(Post)
admin.site.register(Location)
admin.site.register(Category)
