from django.forms import ModelForm
from .models import Census, CensusChangesLog


class CensusForm(ModelForm):
    class Meta:
        model = Census
        fields = ['name']


class CensusChangesLogForm(ModelForm):
    class Meta:
        model = CensusChangesLog
        fields = ['current', 'before', 'issue', 'census']
