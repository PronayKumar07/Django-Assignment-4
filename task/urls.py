from django.urls import path
from . import views
urlpatterns = [

    path('',views.task, name = 'add_task'),
    path('edit/<int:id>', views.edit_task, name = 'edit_task'),
]