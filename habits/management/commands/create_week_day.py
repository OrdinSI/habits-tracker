from django.core.management import BaseCommand

from habits.models import WeekDay


class Command(BaseCommand):
    """Command to create superuser."""

    def handle(self, *args, **options):
        week_days = [
            WeekDay(day=1),  # Monday
            WeekDay(day=2),  # Tuesday
            WeekDay(day=3),  # Wednesday
            WeekDay(day=4),  # Thursday
            WeekDay(day=5),  # Friday
            WeekDay(day=6),  # Saturday
            WeekDay(day=7),  # Sunday
        ]
        WeekDay.objects.bulk_create(week_days)
        self.stdout.write(self.style.SUCCESS("Week days created"))
