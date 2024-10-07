from django.contrib import admin
from .models import Post, Comment

class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text']
    extra = 0

class Postadmin(admin.ModelAdmin):
    list_display = ["title", "is_enable", "publish_field", "created_time", "updated_time"]
    inlines = [CommentAdminInline]

admin.site.register(Post, Postadmin)