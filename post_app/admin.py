from django.contrib import admin
from .models import Post, Like

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'published')

admin.site.register(Post, PostAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')

admin.site.register(Like, LikeAdmin)
