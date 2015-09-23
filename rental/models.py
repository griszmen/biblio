from django.db import models
#from django.contrib.auth.models import User
from shelf.models import BookItem
from django.utils.timezone import now
from django.conf import settings


class Rental(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)  # django.contrib.auth.User
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(default=now)
    returned = models.DateField(null=True, blank=True)

# if isset returned then opis = returned

    def __str__(self):
        return "{who} rented {what} on {when}".format(who=self.who, what=self.what, when=self.when)
