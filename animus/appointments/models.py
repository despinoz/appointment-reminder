from django.db import models as models

from animus.core.models import BaseUUIDModel
from animus.patients.models import Patient
from animus.providers.models import Provider


class Appointment(models.Model):
    # Relationship Fields
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE, related_name="appointments",
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE, related_name="appointments",
    )
    # Fields
    date = models.DateField()
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    def __str__(self):
        return u'%s : %s' % (self.provider, self.patient)
