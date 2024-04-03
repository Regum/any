from django.contrib import admin
from . models.m_debtors import m_debtors
from . models.m_department import department



admin.site.register(m_debtors)
admin.site.register(department)