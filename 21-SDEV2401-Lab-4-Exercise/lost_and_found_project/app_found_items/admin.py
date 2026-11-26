from django.contrib import admin

from .models import FoundItem


@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ("item_name", "found_at", "claimed")
