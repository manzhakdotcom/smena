from datetime import datetime, timedelta

from duty.models import Duty, DutyStaff
from duty.utils import get_duty_datetime


def duty_staff(request):
    dt = get_duty_datetime()
    duty = Duty.objects.filter(date__gte=dt['start'], date__lte=dt['end']).last()

    if duty:
        duty_staff = DutyStaff.objects.filter(duty=duty.pk)
    else:
        duty_staff = False

    return {'duty': duty_staff}


def duty_datetime(request):
    return {'duty_dt': get_duty_datetime()}
