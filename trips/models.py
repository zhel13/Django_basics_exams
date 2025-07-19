from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from traveler.models import Traveler


# Create your models here.
class Trip(models.Model):
    destination = models.CharField(
        validators=[
            MinLengthValidator(3),
            MaxLengthValidator(100)
        ]
    )
    summary = models.TextField()
    start_date = models.DateField(

    )
    duration = models.SmallIntegerField(
        default=1,
        help_text="*Duration in days is expected."
    )
    img_url = models.URLField(
        blank=True,
        null=True,
    )
    traveler = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE,
    )