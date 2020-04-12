from django.contrib import admin
from .models import Appointment


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    fields = ['client', 'clown', 'created_by', 'date_of_appointment', 'rating', 'status', 'report']


admin.site.register(Appointment, AppointmentAdmin)
