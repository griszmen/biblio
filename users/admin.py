from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import BiblioUser
from django.utils.translation import ugettext_lazy as _


class BiblioUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Additional info'), {'fields': ('avatar', 'phone')}),
    )

admin.site.register(BiblioUser, BiblioUserAdmin)

