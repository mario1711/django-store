from django.urls import path
from .views import VistaRegistro , salir , acceder , publicar_resena, CustomPasswordResetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro'  , VistaRegistro.as_view() , name="registro") ,
    path('password_reset', CustomPasswordResetView.as_view(), name='password_reset'), 
    path('salir' , salir , name="salir") ,
    path('acceder' , acceder , name="acceder") , 
    path('publicar_resena', publicar_resena, name='publicar_resena'),
    path('reset/password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
