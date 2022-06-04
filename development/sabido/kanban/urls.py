from django.urls import path
from . import views

urlpatterns = [
    path('todo', views.kanban_todo_form, name = 'kanban_todo_insert'),
    path('doing', views.kanban_doing_form, name = 'kanban_doing_insert'),
    path('done', views.kanban_done_form, name = 'kanban_done_insert'),
    path('todo/<int:id>/', views.kanban_todo_form, name = 'kanban_todo_update'),
    path('doing/<int:id>/', views.kanban_doing_form, name = 'kanban_doing_update'),
    path('done/<int:id>/', views.kanban_done_form, name = 'kanban_done_update'),
    path('list/', views.kanban_list, name = 'kanban_list'),
    path('todo/delete/<int:id>/', views.kanban_todo_delete, name = "kanban_todo_delete"),
    path('doing/delete/<int:id>/', views.kanban_doing_delete, name = "kanban_doing_delete"),
    path('done/delete/<int:id>/', views.kanban_done_delete, name = "kanban_done_delete")
] 


