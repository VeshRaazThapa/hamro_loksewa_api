from django.core.management.base import BaseCommand
from apps.package.models import PackageCategory, PackageSubCategory,Association

class Command(BaseCommand):
    help = "Create package categories and subcategories"

    def handle(self, *args, **options):
        # Define main categories (subjects)
        categories = [
            'Physics',
            'Chemistry',
            'Mathematics',
            'Nepali',
            'English'
        ]
        association = [
             'Association 1'
        ]
        # Define subcategories (levels)
        subcategories = [
            'Primary',
            'Secondary',
            'Higher Secondary',
        ]
        
        # Create main categories
        for category_name in categories:
            category, created = PackageCategory.objects.get_or_create(
                name=category_name
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created category: {category_name}")
                )
            else:
                self.stdout.write(f"Category already exists: {category_name}")
            
        # Create subcategories for each main category
        for subcategory_name in subcategories:
                subcategory, created = PackageSubCategory.objects.get_or_create(
                    name=subcategory_name,
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Created subcategory: {subcategory_name} under {category_name}"
                        )
                    )
                else:
                    self.stdout.write(
                        f"Subcategory already exists: {subcategory_name} under {category_name}"
                    )
        for association_name in association:
                association, created = Association.objects.get_or_create(
                    name=association_name,
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Created Association: {association_name} under {category_name}"
                        )
                    )
                else:
                    self.stdout.write(
                        f"Association already exists: {association_name} under {category_name}"
                    )
        self.stdout.write(
            self.style.SUCCESS("Package categories ,subcategories, Association creation completed")
        )
