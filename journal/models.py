from django.db import models
from datetime import datetime
# Create your models here.


class WriteOut(models.Model):
    data_created = models.DateField(default=datetime.now())
    write_out = models.CharField(widget=forms.Te)