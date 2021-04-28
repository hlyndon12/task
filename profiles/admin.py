from django.contrib import admin
from .models import userModel, pushNotifications

# Register your models here.
admin.site.register(userModel)
admin.site.register(pushNotifications)
