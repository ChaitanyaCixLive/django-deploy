from django.core.management.base import NoArgsCommand

from django_deploy.deploy import tasks


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        for task in tasks:
            task.run()