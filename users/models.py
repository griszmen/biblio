from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

logger = logging.getLogger('django')

class BiblioUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    phone = models.CharField(max_length=15, blank=True, default='')

    class Meta:
        permissions = (
            ('can_rent', 'Can rent a book'),
        )

    # def save(self, *args, **kwargs):
    #     super(BiblioUser, self).save(*args, **kwargs)
    #     try:
    #         p = Permission.objects.get(codename='can_rent')
    #         self.user_permissions.add(p)
    #     except Exception as e:  # Permission does not exist
    #     #logowanie bledu
    #         logger.log(logging.ERROR, e.msg)


@receiver(post_save, sender=BiblioUser)
def add_rent_permission(sender, *args, **kwargs):
    user = kwargs.get('instance')
    try:
        p = Permission.objects.get(codename='can_rent')
        user.user_permissions.add(p)
        logger.log(logging.INFO, "Added ok")
    except Exception as e:
        logger.error("Error jest: %s" % e)
