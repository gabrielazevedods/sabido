from django.urls import path
from . import views

urlpatterns = [
    path('', views.curso_form, name = 'curso_insert'),
    path('<int:id>/', views.curso_form, name = 'curso_update'),
    path('list/', views.curso_list, name = 'curso_list'),
    path('delete/<int:id>/', views.curso_delete, name = "curso_delete")
]

