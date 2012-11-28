from django.db import models
from django.db.models import signals


class CannotRemoveLastAdmin(Exception):
    def __init__(self, env):
        super(CannotRemoveLastAdmin, self).__init__(
            u'Cannot remove the last admin of environment "%s"' % env)


class Environment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField('auth.user', through='UserEnvironment')

    def __unicode__(self):
        return self.name


class UserEnvironment(models.Model):
    environment = models.ForeignKey('Environment')
    user = models.ForeignKey('auth.user')
    is_admin = models.BooleanField()
    default = models.BooleanField()
    creation_datetime = models.DateTimeField(auto_now_add=True)


def admin_required_delete(sender, instance, **kwargs):
    if not instance.is_admin:
        return

    admins = UserEnvironment.objects.filter(environment=instance.environment,
        is_admin=True).exclude(pk=instance.pk).count()

    if not admins:
        raise CannotRemoveLastAdmin(instance)
signals.pre_delete.connect(admin_required_delete, sender=UserEnvironment)
