from django.shortcuts import render
from django.views.generic.edit import CreateView
from . forms.f_add_debtors import add_debtors_form
from . forms.f_add_departments import add_department_form
from django.urls import reverse_lazy
from . models.m_debtors import m_debtors
from . models.m_department import department

import pymorphy2
from pytrovich.enums import NamePart, Gender, Case
from pytrovich.maker import PetrovichDeclinationMaker
maker = PetrovichDeclinationMaker()
from natasha import NamesExtractor, MorphVocab
morph = pymorphy2.MorphAnalyzer()

# Create your views here.
def index(request):
    return render(request, "index.html")


def debtors(request):
    all_debtors = m_debtors.objects.all()
    context = {
        'all_debtors': all_debtors
    }

    return render(request, "debtors.html", context)

def debtor_detail(request, pk):
    
    debtor = m_debtors.objects.get(id=pk)
    debtor_genitive_name = maker.make(NamePart.FIRSTNAME, Gender.MALE, Case.GENITIVE, debtor.name)
    debtor_genitive_surname = maker.make(NamePart.MIDDLENAME, Gender.MALE, Case.GENITIVE, debtor.surname)
    debtor_genitive_lastname = maker.make(NamePart.LASTNAME, Gender.MALE, Case.GENITIVE, debtor.lastname)
    debtor_accusative_name = maker.make(NamePart.FIRSTNAME, Gender.MALE, Case.ACCUSATIVE, debtor.name)
    debtor_accusative_surname = maker.make(NamePart.MIDDLENAME, Gender.MALE, Case.ACCUSATIVE, debtor.surname)
    debtor_accusative_lastname = maker.make(NamePart.LASTNAME, Gender.MALE, Case.ACCUSATIVE, debtor.lastname)

    name_nom = morph.parse(debtor.name)[0].normal_form
    name_gen = morph.parse(debtor.surname)[0].inflect({'gent'}).word
    name_acc = morph.parse(debtor.lastname)[0].inflect({'accs'}).word
    print(name_nom)

    context = {
        'debtor': debtor,
        'debtor_genitive_name': debtor_genitive_name,
        'debtor_genitive_surname': debtor_genitive_surname,
        'debtor_genitive_lastname': debtor_genitive_lastname,
        'debtor_accusative_name': debtor_accusative_name,
        'debtor_accusative_surname': debtor_accusative_surname,
        'debtor_accusative_lastname': debtor_accusative_lastname,

    }
    return render(request, 'debtor_detail.html', context)


def departments(request):
    all_departments = department.objects.all()
    
    context = {
        'all_departments': all_departments
    }
    
    return render(request, "departments.html", context)

def person(request):
    return render(request, "person.html")


class add_debtors_CreateView(CreateView):
    template_name = 'add_debtors.html'
    form_class = add_debtors_form
    success_url = reverse_lazy('debtors')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['department_id'].department.objects.all()
        return context
    

class add_department_CreateView(CreateView):
    template_name = 'add_departments.html'
    form_class = add_department_form
    success_url = reverse_lazy('departments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['department_id'].department.objects.all()
        return context
    
    
