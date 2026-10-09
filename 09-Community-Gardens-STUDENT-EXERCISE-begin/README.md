# SDEV 2401 - ORM, Models, and Migrations

## Part 1: Create Gardens in the Admin Interface

1. Create a virtual environment and install the packages in `requirements.txt`.
2. Add `gardens_app` to the project-level `INSTALLED_APPS` setting.
3. Review the provided `Garden` model and apply its migration.
4. Register `Garden` in `admin.py`.
5. Create a superuser, start the development server, and open `/admin/`.
6. Add these gardens:
   - River Valley Community Garden - Riverdale
   - Prairie Sky Garden - Summerside
   - Mill Creek Garden - Strathcona
   - North Glen Garden - Griesbach
   - Harvest Moon Garden - Terwillegar

## Part 2: Add a `Plant` Model

Create a model with these fields:

- `name`: `CharField` with a maximum length of 100 characters
- `variety`: `CharField` with a maximum length of 100 characters
- `quantity`: `PositiveIntegerField`
- `garden`: `ForeignKey` to `Garden`, with `related_name="plants"` and `on_delete=models.CASCADE`
- `created`: `DateTimeField` with `auto_now_add=True`
- `updated`: `DateTimeField` with `auto_now=True`

Add a `__str__` method that displays the plant name, variety, quantity, and garden. Then create and apply the migration and register `Plant` in the admin interface.

## Part 3: Write Queries in `part_3_queries.py`

1. In `part_3_1_create()`, use `get_or_create()` to add Central Roots Garden in Downtown and return it.
2. In `part_3_2_all()`, return all gardens.
3. In `part_3_3_create()`, add these plants to Central Roots Garden:
   - Tomato, Roma, quantity 12
   - Carrot, Nantes, quantity 24
   - Basil, Genovese, quantity 7
4. In `part_3_4_query()`, return all plants belonging to Central Roots Garden using the `plants` related name.
5. In `part_3_5_less_than()`, return its plants with a quantity below 20.
6. In `part_3_6_ordered()`, return its plants ordered from highest to lowest quantity.
7. In `part_3_7_name_search()`, find plants whose names contain a supplied search term, ignoring case.
8. In `part_3_8_relationship_query()`, query plants through fields on the related garden.
9. In `part_3_9_names()`, return only plant names as a flat list.
10. In `part_3_10_summary()`, return the number of matching plants and whether any exist.

Run the script from the `community_gardens_project` directory:

```text
python part_3_queries.py
```

The functions are deliberately short so each ORM idea can be demonstrated and discussed separately.
