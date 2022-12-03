from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.Signup, name='Signup'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout' ),
    path('index/', views.index, name='index'),
    path('all_emp', views.all_emp, name='all_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('update/<int:id>', views.update, name='updatedata'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    
]