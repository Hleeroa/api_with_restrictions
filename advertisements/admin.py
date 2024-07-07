from django.contrib import admin

from .models import Advertisement

# Register your models here.


@admin.register(Advertisement)
class Advertisement(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'creator', 'created_at']
