from duty.models import Duty, DutyStaff


def duty_staff(request):
    duty_staff = DutyStaff.objects.filter(duty=Duty.objects.all().last().pk)
    return {'duty': duty_staff}