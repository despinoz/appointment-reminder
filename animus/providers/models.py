from django.contrib.auth import get_user_model
from django.db import models as models

from animus.core.models import BaseUUIDModel


User = get_user_model()


class Provider(BaseUUIDModel):
    name = models.CharField(max_length=255)
    last_name_1 = models.CharField(max_length=50)
    last_name_2 = models.CharField(max_length=50)
    known_as = models.CharField(max_length=100)

    nro_colegiatura = models.CharField(max_length=30, blank=True)
    nro_especialista = models.CharField(max_length=30, blank=True)
    specialty = models.CharField(max_length=50, blank=True)
    other_specialty = models.CharField(max_length=50, blank=True)

    users = models.ManyToManyField(User, through='ProviderManager', related_name='providers')

    def __str__(self):
        return u'%s' % self.name


class ProviderManager(BaseUUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s can manage %s" % (self.user, self.provider)
