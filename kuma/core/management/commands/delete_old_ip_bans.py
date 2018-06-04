"""
Delete old revision IPs
"""
from django.core.management.base import BaseCommand

from kuma.core.tasks import delete_old_ip_bans


class Command(BaseCommand):
    help = "Delete old IP Bans"

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            help="How many days 'old' (default 30)",
            default=30,
            type=int)

    def handle(self, *args, **options):
        delete_old_ip_bans(days=options['days'])
