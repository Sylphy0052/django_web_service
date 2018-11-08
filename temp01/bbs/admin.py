from django.contrib import admin

from .models import Comment, Thread

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ThreadAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Thread, ThreadAdmin)
