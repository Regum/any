from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    return render(request, "index.html")



def debtors(request):
    return render(request, "debtors.html")


def departments(request):
    return render(request, "departments.html")