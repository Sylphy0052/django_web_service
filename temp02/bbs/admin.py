from django.contrib import admin

from .models import Bbs, Thread

class ThreadInline(admin.TabularInline):
    model = Thread
    extra = 1

class BbsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Message', {'fields': ['description']}),
    ]
    inlines = [ThreadInline]

admin.site.register(Bbs, BbsAdmin)
