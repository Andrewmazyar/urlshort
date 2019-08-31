from django.db import models

# Create your models here.


class Urlshorter(models.Model):
    url_short = models.CharField(
        max_length=20,
    )
    url_long = models.URLField(
        'URL',
    )
