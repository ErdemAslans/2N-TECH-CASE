from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_authorized_personnel', 'annual_leave')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_authorized_personnel', 'annual_leave')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
