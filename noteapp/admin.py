from django.contrib import admin
from .models import Note, Alarm
    
# Register your models here.
admin.site.register(Note)
admin.site.register(Alarm)