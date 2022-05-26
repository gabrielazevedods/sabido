from django.urls import path
from . import views

urlpatterns = [
    path('', views.disciplinas_form, name = 'disciplinas_insert'),
    path('<int:id>/', views.disciplinas_form, name = 'disciplinas_update'),
    path('list/', views.disciplinas_list, name = 'disciplinas_list'),
    path('delete/<int:id>/', views.disciplinas_delete, name = "disciplinas_delete")
]

