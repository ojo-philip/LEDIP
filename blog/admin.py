from django.contrib import admin
from .models import Category, Post

admin.site.site_header = "LEDIP Administration"

class PostAdmin(admin.ModelAdmin):

  list_display = ["title", 'timestamp', 'status']
  list_filter = ["title", 'timestamp', 'content', 'status']


# Register your models here.
admin.site.register(Category)
admin.site.register(Post, PostAdmin)