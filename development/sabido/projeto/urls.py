from django.urls import path
from . import views

urlpatterns = [
    path('', views.projeto_form, name = 'projeto_insert'),
    path('<int:id>/', views.projeto_form, name = 'projeto_update'),
    path('list/', views.projeto_list, name = 'projeto_list'),
    path('delete/<int:id>/', views.projeto_delete, name = "projeto_delete")
]

