from django.contrib import admin
from django import forms
from .models import Provider


class ProviderAdminForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = '__all__'


class ProviderAdmin(admin.ModelAdmin):
    form = ProviderAdminForm
    list_display = ['name', 'last_name_1', 'last_name_2', 'known_as', 'nro_colegiatura',
                    'nro_especialista', 'specialty', 'other_specialty']


admin.site.register(Provider, ProviderAdmin)
