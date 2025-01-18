from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Run all management commands"

    def handle(self, *args, **options):
        # List all your management commands here
        commands = [
            'create_province',
            'create_groups',
            'create_areas_of_preparation',
            'create_package_category'
        ]

        for command in commands:
            self.stdout.write(f"Running command: {command}")
            call_command(command)
            self.stdout.write(self.style.SUCCESS(f"Completed: {command}\n"))