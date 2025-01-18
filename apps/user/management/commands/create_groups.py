from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help_text = "Create user groups"

    def handle(self, **options):
        groups = [
            {"id": 1, "name": "Admin", "type": "Admin"},
            {"id": 2, "name": "Student", "type": "Admin"},
            {"id": 3, "name": "Teacher", "type": "Admin"},
        ]
        for item in groups:
            # print(item)
            Group.objects.get_or_create(name=item['name'], id=item['id'])
            self.stdout.write(self.style.SUCCESS("Group {} created successfully".format(item)))
        