from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.urls import reverse


class Profile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, blank=True)
    email = models.EmailField(_('email_address'), unique=True, max_length=200)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='avatars/%Y/%M/%D', default='avatars/avatar.jpg', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_pk': 'pk'})


def is_staff(self):
    return self.staff


@property
def is_admin(self):
    return self.admin


def __str__(self):
    return self.email
