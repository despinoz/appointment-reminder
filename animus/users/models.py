from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import BooleanField, CharField, EmailField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from animus.core.models import BaseModel

from .managers import UserManager


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    first_name = CharField(_("Name of User"), blank=True, max_length=50)
    last_name = CharField(
        _("Last name of User"),
        blank=True,
        max_length=150)

    email = EmailField(_('email address'), unique=True)
    is_staff = BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"email": self.email})
