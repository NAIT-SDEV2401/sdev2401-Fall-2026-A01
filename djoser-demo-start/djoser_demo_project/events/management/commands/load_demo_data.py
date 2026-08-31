from django.core.management.base import BaseCommand
from events.models import Event, Talk
from datetime import datetime, timezone


class Command(BaseCommand):
    help = "Load initial demo data for events and talks."

    def handle(self, *args, **kwargs):
        # Clear existing data so the command is safe to run more than once
        Talk.objects.all().delete()
        Event.objects.all().delete()

        # Event 1 — PyCon Demo Day
        event1 = Event.objects.create(
            name="PyCon Demo Day",
            description="Annual Python conference demo day showcasing new projects.",
            location="Ottawa, ON",
            start_date="2025-06-01",
            end_date="2025-06-03",
        )
        Talk.objects.create(
            event=event1,
            title="Intro to FastAPI",
            description="A comparison of FastAPI and DRF for building REST APIs.",
            speaker_name="Maria Chen",
            status="confirmed",
            scheduled_time=datetime(2025, 6, 1, 9, 0, tzinfo=timezone.utc),
        )
        Talk.objects.create(
            event=event1,
            title="Async Django",
            description="Exploring Django's async capabilities and when to use them.",
            speaker_name="James Okafor",
            status="scheduled",
            scheduled_time=datetime(2025, 6, 2, 14, 0, tzinfo=timezone.utc),
        )

        # Event 2 — Django Girls Workshop
        event2 = Event.objects.create(
            name="Django Girls Workshop",
            description="Beginner-friendly workshop introducing Django to new developers.",
            location="Toronto, ON",
            start_date="2025-07-15",
            end_date="2025-07-15",
        )
        Talk.objects.create(
            event=event2,
            title="Your First Django App",
            description="Step-by-step guide to building a Django app from scratch.",
            speaker_name="Sofia Reyes",
            status="confirmed",
            scheduled_time=datetime(2025, 7, 15, 10, 0, tzinfo=timezone.utc),
        )
        Talk.objects.create(
            event=event2,
            title="Django ORM Basics",
            description="How to query your database using the Django ORM.",
            speaker_name="Priya Nair",
            status="confirmed",
            scheduled_time=datetime(2025, 7, 15, 13, 0, tzinfo=timezone.utc),
        )

        # TODO Part 2: Add event3 — "REST API Summit"
        # event3 = Event.objects.create(
        #     name="REST API Summit",
        #     description="Conference focused on API design and best practices.",
        #     location="Vancouver, BC",
        #     start_date="2025-09-10",
        #     end_date="2025-09-12",
        # )
        # Talk.objects.create(
        #     event=event3,
        #     title="Building APIs with Djoser",
        #     description="A walkthrough of token authentication using Djoser and Django REST Framework.",
        #     speaker_name="Alex Rivera",
        #     status="scheduled",
        #     scheduled_time=datetime(2025, 9, 10, 10, 0, tzinfo=timezone.utc),
        # )

        self.stdout.write(self.style.SUCCESS("Demo data loaded successfully."))
