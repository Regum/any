from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^debtors', views.debtors, name='debtors'),
    path('add/', views.add_debtors_CreateView.as_view(), name='add_debtors'),
    re_path(r'^departments', views.departments, name='departments'),
    path('add_department/', views.add_department_CreateView.as_view(), name='add_department'),

]
