from django.db.models import CharField, EmailField
from django.db import models as models

from animus.core.models import BaseUUIDModel


class Patient(BaseUUIDModel):
    name = models.CharField(max_length=255)
    last_name_1 = models.CharField(max_length=30)
    last_name_2 = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    cellphone = models.CharField(max_length=30, blank=True)
    dni = models.CharField(max_length=20)

    def __unicode__(self):
        return u'%s' % self.pk
