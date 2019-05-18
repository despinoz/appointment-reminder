from django.contrib import admin
from django import forms
from .models import Patient

class PatientAdminForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'


class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm
    list_display = ['name', 'last_name_1', 'last_name_2', 'email', 'phone', 'cellphone', 'dni']
    readonly_fields = ['name', 'last_name_1', 'last_name_2', 'email', 'phone', 'cellphone', 'dni']

admin.site.register(Patient, PatientAdmin)
