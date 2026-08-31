from django.contrib import admin
from .models import Event, Talk


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "start_date", "end_date")


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = ("title", "event", "speaker_name", "status", "scheduled_time")
