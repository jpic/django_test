from django.db import models


class Widget(models.Model):
    user = models.ForeignKey('auth.user', null=True, blank=True)
