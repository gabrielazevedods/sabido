from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cursos_form, name = 'cursos_insert'),
    path('<int:id>/', views.Cursos_form, name = 'cursos_update'),
    path('list/', views.Cursos_list, name = 'cursos_list'),
    path('delete/<int:id>/', views.Cursos_delete, name = "cursos_delete")
]

