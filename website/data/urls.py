from django.urls import path
from . import  views


urlpatterns = [   
    path('', views.home, name='home'),   
    path('profil/', views.profil, name='profile'),
    path('kontak/', views.kontak, name='kontak'),
    path('product/', views.product, name='product'),
    path('custemer/<str:pk>/', views.custemer, name='custemer'),
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('create_custemer/', views.createCustemer, name='create_custemer'),
    path('update_custemer/<str:pk>/', views.updateCustemer, name='update_custemer'),
    path('delete_custemer/<str:pk>/', views.deleteCustemer, name="delete_custemer"),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('registrasi/', views.Registrasi, name='registrasi'),
    

]
