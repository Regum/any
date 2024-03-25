from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    return TemplateResponse(request, 'index.html')



def debtors(request):
    return TemplateResponse(request, 'debtors.html')


def departments(request):
    return TemplateResponse(request, 'departments.html')