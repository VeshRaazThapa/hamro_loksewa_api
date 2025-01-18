from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from apps.user.models import AreasOfPreparations

class Command(BaseCommand):
    help_text = "Createareas of preparation"

    def handle(self, **options):
        groups = [
            {"id": 1, "name": "Loksewa", "icon": ""},
            {"id": 2, "name": "Sikshak Sewa", "icon": ""},
            {"id": 3, "name": "Nepal Police", "icon": ""},
            {"id": 4, "name": "Nepal Bank", "icon": ""},
            {"id": 5, "name": "Nepal Engineering", "icon": ""},
            {"id": 6, "name": "Nepal Health Service", "icon": ""},
            {"id": 7, "name": "Nepal Telecommunication", "icon": ""},

        ]
        for item in groups:
            # print(item)
            AreasOfPreparations.objects.get_or_create(name=item['name'], id=item['id'])
            self.stdout.write(self.style.SUCCESS("AreasOfPreparations {} created successfully".format(item)))
        