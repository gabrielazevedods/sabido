from django.urls import path
from . import views

urlpatterns = [
    path('', views.compromisso_form, name = 'compromisso_insert'),
    path('<int:id>/', views.compromisso_form, name = 'compromisso_update'),
    path('list/', views.compromisso_list, name = 'compromisso_list'),
    path('delete/<int:id>/', views.compromisso_delete, name = "compromisso_delete")
]

