from django.utils import timezone


def get_current_time():
    """Function for getting current time"""
    return timezone.now().time()
