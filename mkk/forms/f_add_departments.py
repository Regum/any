from django.forms import ModelForm
from ..models.m_department import department


class add_department_form(ModelForm):
    class Meta:
        model = department
        fields = ('name','letter')

