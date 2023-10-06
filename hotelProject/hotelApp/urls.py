from django.urls import path

from hotelApp import views


urlpatterns = [
    
    path('roomlist', views.roomList, name='roomList'),
    path('roomdetails/<int:pk>', views.roomDetails, name='roomDetails'),

    path('bookList', views.bookList, name='bookList'),
    path('delete/<int:pk>', views.deleteBook, name='deletebook'),
    path('addBenefit/<int:pk>', views.addBenefit, name='addBenefit'),

]

