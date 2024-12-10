from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel
from django.conf import settings
from django.db import models
import random

User = get_user_model() # get the current user model



def code_generator(length=5):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for _ in range(length))


class RegistrationProfile(TimeStampedModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='registration_profile'
        )
    code = models.CharField(
        verbose_name='code',
        help_text='random code used for registration and for password reset',
        max_length=15,
        default=code_generator
    )
    code_type = models.CharField(
        verbose_name='code type',
        max_length=2,
        choices=(
            ('RV', 'Registration Validation'),
            ('PR', 'Password Reset')
        )
    )
    code_used = models.BooleanField(
        verbose_name='code used',
        default=False
    )

    def __str__(self):
        return f'{self.user.email}, {self.code}'