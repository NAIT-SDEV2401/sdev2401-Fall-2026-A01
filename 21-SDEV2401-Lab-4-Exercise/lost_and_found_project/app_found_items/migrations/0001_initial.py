from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FoundItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("item_name", models.CharField(blank=True, max_length=200)),
                ("found_at", models.CharField(max_length=200)),
                ("claimed", models.BooleanField(default=False)),
            ],
        ),
    ]
