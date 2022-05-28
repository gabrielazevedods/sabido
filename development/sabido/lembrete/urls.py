from django.urls import path
from . import views

urlpatterns = [
    path('', views.lembrete_form, name = 'lembrete_insert'),
    path('<int:id>/', views.lembrete_form, name = 'lembrete_update'),
    path('list/', views.lembrete_list, name = 'lembrete_list'),
    path('delete/<int:id>/', views.lembrete_delete, name = "lembrete_delete")
]


