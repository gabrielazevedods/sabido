from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos_form, name = 'cursos_insert'),
    path('<int:id>/', views.cursos_form, name = 'cursos_update'),
    path('list/', views.cursos_list, name = 'cursos_list'),
    path('delete/<int:id>/', views.cursos_delete, name = "cursos_delete")
]

