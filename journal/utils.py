from journal.models import WriteDown, WriteOut, ExtraWriteOut


def get_write_downs_with_details():
    write_downs = WriteDown.objects.all().order_by('date', 'time')

    return set_extra_properties(write_downs.is_published())


def get_write_downs():
    write_downs = WriteDown.objects.all().order_by('date', 'time')

    return write_downs.is_published()


def get_extra_write_outs():
    extra_write_outs = ExtraWriteOut.objects.all()

    return extra_write_outs.is_published()


def get_write_outs():
    write_outs = WriteOut.objects.all()

    return write_outs.is_published()


def set_extra_properties(all_write_down):
    all_write_out = get_write_outs()
    all_extra_write_out = get_extra_write_outs()

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
    write_out = WriteOut.objects.filter(write_down=write_down_id).is_published()
    if write_out:
        return True
    return False


def is_extra_write_out(write_down_id):
    extra_write_out = ExtraWriteOut.objects.filter(write_down=write_down_id).is_published()
    if extra_write_out:
        return True
    return False
