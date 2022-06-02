from django.urls import path
from . import views

urlpatterns = [
    path('', views.aluno_form, name = 'aluno_insert'),
    path('<int:id>/', views.aluno_form, name = 'aluno_update'),
    path('list/', views.aluno_list, name = 'aluno_list'),
    path('delete/<int:id>/', views.aluno_delete, name = "aluno_delete")
]

