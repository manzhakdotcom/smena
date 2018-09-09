from datetime import datetime, timedelta

from duty.models import Duty

def is_duty():
    duty_datetime = Duty.objects.all().last().date
    dt_tday = datetime.now()
    dt_8am = datetime(dt_tday.year, dt_tday.month, dt_tday.day, 8)
    dt_8pm = datetime(dt_tday.year, dt_tday.month, dt_tday.day, 20)

    if dt_tday > dt_8pm:
        start_duty = dt_8pm
        finish_duty = dt_8pm + timedelta(0, 12*60*60)
    elif dt_tday < dt_8am:
        start_duty = dt_8am - timedelta(0, 12*60*60)
        finish_duty = dt_8am
    else:
        start_duty = dt_8am
        finish_duty = dt_8pm

    return 'с {}:{} {}.{}.{} по {}:{} {}.{}.{}'.format(
                                                        start_duty.strftime('%H'),
                                                        start_duty.strftime('%M'),
                                                        start_duty.strftime('%d'),
                                                        start_duty.strftime('%m'),
                                                        start_duty.strftime('%Y'),
                                                        finish_duty.strftime('%H'),
                                                        finish_duty.strftime('%M'),
                                                        finish_duty.strftime('%d'),
                                                        finish_duty.strftime('%m'),
                                                        finish_duty.strftime('%Y')