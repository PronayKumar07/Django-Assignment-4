from django.urls import path
from . import views
urlpatterns = [

    path('',views.category, name = 'add_category'),
    path('delete/<int:id>', views.delete_category, name = 'delete_task')

]