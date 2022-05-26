from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefa_form, name = 'tarefa_insert'),
    path('<int:id>/', views.tarefa_form, name = 'tarefa_update'),
    path('list/', views.tarefa_list, name = 'tarefa_list'),
    path('delete/<int:id>/', views.tarefa_delete, name = "tarefa_delete")
]

