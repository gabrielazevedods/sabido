from django.urls import path
from . import views

urlpatterns = [
    path('', views.disciplina_form, name = 'disciplina_insert'),
    path('<int:id>/', views.disciplina_form, name = 'disciplina_update'),
    path('list/', views.disciplina_list, name = 'disciplina_list'),
    path('delete/<int:id>/', views.disciplina_delete, name = "disciplina_delete")
] 


