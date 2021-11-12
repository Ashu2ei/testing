from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin , BaseUserManager , AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext as _


class MyUserManager(UserManager):
    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email address is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
       
    username = None
    email = models.EmailField(blank=False, unique=True)
    email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return str(self.email)    
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    