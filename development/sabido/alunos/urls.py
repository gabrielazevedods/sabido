from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunos_form, name = 'alunos_insert'),
    path('<int:id>/', views.alunos_form, name = 'alunos_update'),
    path('list/', views.alunos_list, name = 'alunos_list'),
    path('delete/<int:id>/', views.alunos_delete, name = "alunos_delete")
]