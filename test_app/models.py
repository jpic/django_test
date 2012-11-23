from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField('Member')

    def __unicode__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

