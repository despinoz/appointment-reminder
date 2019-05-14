import uuid

from django.db import models

from model_utils.models import SoftDeletableModel, TimeStampedModel


class BaseModel(TimeStampedModel):
    """
    BaseModel inherits from models.TimeStampedModel and implements the
    following fields for
    base information:
        * uuid
        * modified [from TimeStampedModel]
        * created [from TimeStampedModel]
    """
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class SoftDeleteBaseModel(BaseModel, SoftDeletableModel):

    class Meta:
        abstract = True
