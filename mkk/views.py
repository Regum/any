from django.shortcuts import render
from django.views.generic.edit import CreateView
from . forms.f_add_debtors import add_debtors_form
from . forms.f_add_departments import add_department_form
from django.urls import reverse_lazy
from . models.m_debtors import m_debtors
from . models.m_department import department



import pymorphy3
morph = pymorphy3.MorphAnalyzer()

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
    debtors = m_debtors.objects.get(id=pk)
    # Винительный падеж
    declined_surname_g = morph.parse(debtors.surname)[0].inflect({'gent'}).word
    declined_name_g = morph.parse(debtors.name)[0].inflect({'gent'}).word
    declined_lastname_g = morph.parse(debtors.lastname)[0].inflect({'gent'}).word
    declined_surname_a = morph.parse(debtors.surname)[0].inflect({'accs'}).word
    declined_name_a = morph.parse(debtors.name)[0].inflect({'accs'}).word
    declined_lastname_a = morph.parse(debtors.lastname)[0].inflect({'accs'}).word

    context = {
        "debtors": debtors,
        "declined_surname_g": declined_surname_g.capitalize(),
        "declined_name_g": declined_name_g.capitalize(),
        "declined_lastname_g": declined_lastname_g.capitalize(),
        "declined_surname_a": declined_surname_a.capitalize(),
        "declined_name_a": declined_name_a.capitalize(),
        "declined_lastname_a": declined_lastname_a.capitalize()
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
    
    
