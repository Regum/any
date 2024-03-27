from django.shortcuts import render
from django.views.generic.edit import CreateView
from . forms.f_add_debtors import add_debtors_form
from . forms.f_add_departments import add_department_form
from django.urls import reverse_lazy
from . models.m_debtors import m_debtors
from . models.m_department import department



# Create your views here.
def index(request):
    return render(request, "index.html")


def debtors(request):
    all_debtors = m_debtors.objects.all()
    context = {
        'all_debtors': all_debtors
    }
    return render(request, "debtors.html", context)


def departments(request):
    all_departments = department.objects.all()
    context = {
        'all_departments': all_departments
    }
    return render(request, "departments.html", context)


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