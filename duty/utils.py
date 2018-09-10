from datetime import datetime, timedelta
import pytz

from django.utils import timezone


def get_duty_datetime():
    dt_now = timezone.now()
    _8am = datetime(dt_now.year, dt_now.month, dt_now.day, 8, 0, 0, 00000, pytz.UTC)
    _8pm = datetime(dt_now.year, dt_now.month, dt_now.day, 20, 0, 0, 00000, pytz.UTC)

    if dt_now > _8pm:
        start_duty_datetime = _8pm
        end_duty_datetime = _8pm + timedelta(0, 12 * 60 * 60)
    elif dt_now < _8am:
        start_duty_datetime = _8am - timedelta(0, 12 * 60 * 60)
        end_duty_datetime = _8am
    else:
        start_duty_datetime = _8am
        end_duty_datetime = _8pm

    time = {'start': start_duty_datetime, 'end': end_duty_datetime}

    return time
