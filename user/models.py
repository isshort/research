from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.managers import UserManager
from utils.herlpers import upload_instance
from utils.regax import (
    phone_regex
)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(verbose_name=_('phone number'),
                             max_length=15, unique=True, null=True, validators=[phone_regex], )
    fullname = models.CharField(verbose_name=_('full name'),
                                max_length=30)
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(
        upload_to=upload_instance, default="account.png", blank=True)
    objects = UserManager()
    verified = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['fullname', ]
    USERNAME_FIELD = 'phone'

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.fullname or self.phone

    def clean(self):
        super(User, self).clean()
        if not self.phone:
            raise ValidationError(_('Provide at least phone'))
