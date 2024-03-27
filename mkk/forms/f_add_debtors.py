from django.forms import ModelForm
from ..models.m_debtors import m_debtors



class add_debtors_form(ModelForm):
    class Meta:
        model = m_debtors
        fields = ('department','surname', 'name', 'lastname', 'date_birth', 'place_birth', 'contract_number', 'agreement_date', 'loan_amount')