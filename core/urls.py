from django.urls import path # type: ignore
from .views import home, save, update, updating, delete,register,login, toAssess, logout, updateMyCar
from django.conf import settings # type: ignore


urlpatterns = [
    path('home', home, name='home'),
    path('save', save, name='save'),
    path('update/<int:id>', update, name='update'),
    path('updating/<int:id>', updating, name='updating'),
    path('delete/<int:id>', delete, name='delete'),
    path('register/', register, name='register'),
    path('login/', login ,name = 'login'),
    path('toAssess/<int:id>', toAssess, name='toAssess'),
    path('logout/', logout, name = 'logout'),
    path('updateMyCar/<int:id>', updateMyCar, name = 'updateMyCar'),

    
   
] 

