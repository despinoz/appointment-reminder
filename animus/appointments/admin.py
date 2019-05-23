from django.contrib import admin
from django import forms
from animus.appointments.models import Appointment

class AppointmentAdminForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentAdminForm
    list_display = ['provider', 'patient', 'date', 'start_time', 'end_time']

admin.site.register(Appointment, AppointmentAdmin)
