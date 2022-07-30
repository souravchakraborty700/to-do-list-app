from django.contrib import admin
from qtpy import _warn_old_minor_version
from .models import Task

admin.site.register(Task)



