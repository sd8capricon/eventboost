from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

# Register your models here.
admin.site.register(Account)
# admin.site.register(Account, UserAdmin)
