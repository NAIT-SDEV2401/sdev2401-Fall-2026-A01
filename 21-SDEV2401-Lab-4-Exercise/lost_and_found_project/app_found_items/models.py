from django.db import models


class FoundItem(models.Model):
    item_name = models.CharField(max_length=200, blank=True)
    found_at = models.CharField(max_length=200)
    claimed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item_name} ({self.found_at})"
