from django.urls import path
from . import views 
from .views import anadir_producto , mostrar_resenas

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/anadir' , anadir_producto , name="anadir_producto") ,
    path('review/show' , mostrar_resenas , name="sidebar") , 
    
]