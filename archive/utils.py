from journal.models import WriteDown, WriteOut, ExtraWriteOut
from django.db.models import Q


def get_all_write_down(date_from, date_to):
    all_write_down = WriteDown.objects.filter(Q(date__gte=date_from, date__lte=date_to))
    return set_extra_properties(all_write_down)


def set_extra_properties(all_write_down):
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


def is_write_out(write_down_id):
    write_out = WriteOut.objects.filter(write_down=write_down_id)
    if write_out:
        return True
    return False


def is_extra_write_out(write_down_id):
    extra_write_out = ExtraWriteOut.objects.filter(write_down=write_down_id)
    if extra_write_out:
        return True
    return False
