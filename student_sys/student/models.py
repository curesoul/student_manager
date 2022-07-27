from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (1, 'male'),
        (2, 'female'),
        (0, 'unknown'),
    ]
    STATUS_ITEMS = [
        (0, 'apply'),
        (1, 'allow'),
        (2, 'deny'),
    ]

