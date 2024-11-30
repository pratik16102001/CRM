from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser):
    MALE = "male"
    FEMALE = "female"
    NOT_SPECIFIED = "Not Specified"

    GENDER_CHOICES = ((MALE, MALE), (FEMALE, FEMALE), (NOT_SPECIFIED, NOT_SPECIFIED))

    gender = models.CharField(
        max_length=15, null=True, blank=True, choices=GENDER_CHOICES
    )
    country = models.CharField(max_length=15, null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)
    langauge = models.CharField(max_length=15, null=True, blank=True)

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
