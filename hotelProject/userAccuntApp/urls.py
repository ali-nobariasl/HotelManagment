from django.urls import path ,include

from userAccuntApp import views

urlpatterns = [

    path('', views.registerGuest, name='registerGuest'),

    path('register/',views.register, name="register"),
    path('login/',views.my_login, name="my_login"),
    path('logout/',views.log_out, name="log_out"),
    
]