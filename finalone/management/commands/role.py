from django.core.management.base import BaseCommand
from finalone.models import Role

class Command(BaseCommand):
    help = 'Create default roles in the database'

    def handle(self, *args, **kwargs):
        roles = [
            {"name": "admin", "description": "Administrator with full access"},
            {"name": "employee", "description": "Regular employee with limited access"},
        ]

        for role_data in roles:
            role, created = Role.objects.get_or_create(
                name=role_data['name'],
                defaults={'description': role_data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Role "{role.name}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Role "{role.name}" already exists.'))

