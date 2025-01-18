from django.core.management.base import BaseCommand
from apps.package.models import Province


class Command(BaseCommand):
    help = "Create provinces"

    def handle(self, *args, **options):
        provinces = [
            "Province 1",
            "Province 2",
            "Province 3",
            "Province 4",
            "Province 5",
            "Province 6",
            "Province 7"
        ]
        
        for province_name in provinces:
            province, created = Province.objects.get_or_create(name=province_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created province: {province_name}"))
            else:
                self.stdout.write(f"Province already exists: {province_name}")
        
        self.stdout.write(self.style.SUCCESS("Province creation completed"))