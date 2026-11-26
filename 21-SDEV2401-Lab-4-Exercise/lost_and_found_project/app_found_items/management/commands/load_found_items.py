from django.core.management.base import BaseCommand

from app_found_items.models import FoundItem


class Command(BaseCommand):
    help = "Add sample found items to the local database."

    def handle(self, *args, **options):
        samples = [
            ("Blue water bottle", "Library study area", False),
            ("Black umbrella", "Student Centre entrance", False),
            ("Calculator in a grey case", "Science Building room 204", True),
        ]
        added = 0

        for item_name, found_at, claimed in samples:
            if FoundItem.objects.filter(item_name=item_name, found_at=found_at).exists():
                continue
            FoundItem.objects.create(item_name=item_name, found_at=found_at, claimed=claimed)
            added += 1

        self.stdout.write(self.style.SUCCESS(f"Added {added} sample found item(s)."))
