from django.shortcuts import render
from django.views.generic.edit import CreateView
from . forms.f_add_debtors import add_debtors_form
from . forms.f_add_departments import add_department_form
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, "index.html")


def debtors(request):
    return render(request, "debtors.html")


def departments(request):
    return render(request, "departments.html")


class add_debtors_CreateView(CreateView):
    template_name = 'add_debtors.html'
    form_class = add_debtors_form
    success_url = reverse_lazy('add_debtors')
    
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