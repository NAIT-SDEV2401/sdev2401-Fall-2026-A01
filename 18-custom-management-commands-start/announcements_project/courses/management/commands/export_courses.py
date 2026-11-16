import csv
from django.core.management.base import BaseCommand
from courses.models import Course

class Command(BaseCommand):
    help = 'Export courses to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('output_file', type=str, help='The path to the output CSV file')

    def handle(self, *args, **kwargs):
        output_file = kwargs.get('output_file')
        if not output_file:
            self.stdout.write(self.style.ERROR('Please provide an output file path'))
            return

        courses = Course.objects.all()
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'description'])  # Write header
            for course in courses:
                writer.writerow([course.title, course.description])

        self.stdout.write(
            self.style.SUCCESS(
                F'Successfully exported {courses.count()} courses to {output_file}'
            )
        )
