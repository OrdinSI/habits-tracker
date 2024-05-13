import requests

from django.utils import timezone

from config import settings
from habits.models import Habit
import logging

logger = logging.getLogger(__name__)


def send_message(chat_id, message):
    """Function for sending message to user"""

    data = {"chat_id": chat_id, "text": message}

    url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
    response = requests.post(url, data=data)
    return response


def check_habits():
    """Function for checking habits"""
    try:
        habits = Habit.objects.filter(is_pleasant=False, owner__chat_id__isnull=False)
        current_time = timezone.now()
        current_local_time = current_time.astimezone(timezone.get_current_timezone())
        date_now = current_local_time.today()
        for habit in habits:
            if habit.date == date_now or not habit.date:
                if habit.time >= current_local_time.time():
                    message = (
                        f"В {habit.time} необходимо выполнить привычку: {habit.action}"
                    )
                    if habit.linked_habit:
                        message += (
                            f"\n\nСвязанная привычка: {habit.linked_habit.action}"
                        )
                    elif habit.reward:
                        message += f"\n\nНаграда: {habit.reward}"
                    else:
                        message += "\n\nНаграда отсутствует"
                    send_message(habit.owner.chat_id, message)
                habit.date = date_now + timezone.timedelta(days=habit.periodicity)
                habit.save()
    except Exception as e:
        print(f"Error: {e}")
