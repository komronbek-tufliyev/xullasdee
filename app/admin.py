from django.contrib import admin
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.
