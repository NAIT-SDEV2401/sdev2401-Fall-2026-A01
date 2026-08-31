from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Talk(models.Model):
    STATUS_CHOICES = (
        ("scheduled", "Scheduled"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="talks")
    title = models.CharField(max_length=200)
    description = models.TextField()
    speaker_name = models.CharField(max_length=150)  # plain CharField — no FK to User, keeps Part 3 simple
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ({self.event.name})"
