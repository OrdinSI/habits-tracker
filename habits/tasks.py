from celery import shared_task
from habits.services import check_habits


@shared_task
def habit_scheduler():
    """Function for checking habits"""
    check_habits()
