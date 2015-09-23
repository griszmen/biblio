from django.contrib import admin
from .models import Rental


class RentalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rental, RentalAdmin)
