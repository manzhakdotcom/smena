from datetime import datetime, timedelta

from duty.models import Duty, DutyStaff
from duty.utils import get_duty_datetime


def duty_staff(request):
    duty_datetime = get_duty_datetime()
    duty = Duty.objects.filter(date__range=[duty_datetime['start'], duty_datetime['end']])
    if duty.exists():
        duty_staff = DutyStaff.objects.filter(duty=duty.pk)
    else:
        duty_staff = False

    return {'duty': duty_staff}


def duty_datetime(request):
    dt_now = datetime.now()
    _8am = datetime(dt_now.year, dt_now.month, dt_now.day, 8)
    _8pm = datetime(dt_now.year, dt_now.month, dt_now.day, 20)

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

    return {'duty_dt': time}
