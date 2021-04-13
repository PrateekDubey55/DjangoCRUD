from django.urls import path 
from . import views

app_name='studentcrud'
urlpatterns = [
    path('',views.emp, name="index"),
    path('show',views.show, name="show"),  
    path('edit/<int:id>', views.edit, name="edit"),  
    path('update/<int:id>', views.update, name="update"),  
    path('delete/<int:id>', views.destroy, name="delete"),
]