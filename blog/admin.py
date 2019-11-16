from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['id', 'title', 'author', 'created_date', 'published_date']
    list_filter = ['created_date', 'published_date']
    list_editable = ['title', 'author']


admin.site.register(Post, PostAdmin)
