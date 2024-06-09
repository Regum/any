from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static




from . import views



urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^debtors', views.debtors, name='debtors'),
    path('debtor/<int:pk>/', views.debtor_detail, name='debtor_detail'),
    path('download/', views.working_with_file.as_view(), name='download'),
    path('add/', views.add_debtors_CreateView.as_view(), name='add_debtors'),
    re_path(r'^departments', views.departments, name='departments'),
    path('add_department/', views.add_department_CreateView.as_view(), name='add_department'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
