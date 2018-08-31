from datetime import datetime

from journal.models import WriteDown, WriteOut, ExtraWriteOut


def set_properties_to_write_down():
    all_write_down = WriteDown.objects.all()
    all_write_out = WriteOut.objects.all()
    all_extra_write_out = ExtraWriteOut.objects.all()

    for write_down in all_write_down:
            write_down.is_write_out = False
            write_down.is_extra_write_out = False
            for write_out in all_write_out:
                if write_down.id == write_out.write_down_id:
                    write_down.is_write_out = True
            for extra_write_out in all_extra_write_out:
                if write_down.id == extra_write_out.write_down_id:
                    write_down.is_extra_write_out = True
    
    return all_write_down

def get_duty_time():
    dt_now = datetime.now()
    dt_08_00 = datetime(dt_now.year, dt_now.month, dt_now.day, 8)
    dt_20_00 = datetime(dt_now.year, dt_now.month, dt_now.day, 20)

    if dt_20_00 > dt_now > dt_08_00:
        return 'Записи СЦБ - с 08:00 {}.{}.{} по 20:00 {}.{}.{}'.format(dt_now.day, dt_now.month, dt_now.year, dt_now.day, dt_now.month, dt_now.year)
