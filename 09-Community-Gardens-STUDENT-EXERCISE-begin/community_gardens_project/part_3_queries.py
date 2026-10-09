#!/usr/bin/env python

### ! Do not edit ! ###
import os

import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "community_gardens_project.settings",
)
django.setup()

print("Django environment set up successfully.")


from gardens_app.models import Garden, Plant


def part_3_1_create():


def part_3_2_all():


def part_3_3_create():


def part_3_4_query():


def part_3_5_less_than():


def part_3_6_ordered():


def part_3_7_name_search(search_term):


def part_3_8_relationship_query():


def part_3_9_names():


def part_3_10_summary():


def display_plants(plants):
    return [
        f"{plant.name} ({plant.variety}) - {plant.quantity}"
        for plant in plants
    ]


def run():
    print("Running the community gardens ORM prep.")

    part_3_1_create()
    gardens = part_3_2_all()
    print(f"Gardens in the database: {[garden.name for garden in gardens]}")

    part_3_3_create()
    print(f"Plants for Central Roots Garden: {display_plants(part_3_4_query())}")
    print(f"Plants with quantity below 20: {display_plants(part_3_5_less_than())}")
    print(f"Plants ordered by quantity: {display_plants(part_3_6_ordered())}")
    print(f"Plant-name search for 'to': {display_plants(part_3_7_name_search('to'))}")
    print(f"Plants found through Garden fields: {display_plants(part_3_8_relationship_query())}")
    print(f"Plant names only: {list(part_3_9_names())}")
    print(f"Plant summary: {part_3_10_summary()}")


if __name__ == "__main__":
    run()
