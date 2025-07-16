from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from traveler import validators

# Create your models here.
class Traveler(models.Model):
    nickname = models.CharField(
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(30),
            validators.NicknameValidator,
        ],
        help_text='*Nicknames can contain only letters and digits.'
    )
    email = models.EmailField(
        max_length=30,
    )
    country = models.CharField(
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(3),
        ]
    )
    about_me = models.TextField(
        blank=True,
        null=True,
    )