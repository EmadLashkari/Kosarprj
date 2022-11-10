from re import I
from django.urls import path
from . import views

app_name = 'modir'
urlpatterns = [
    path('', views.LoginView ,name='login'),
    path('home/', views.home, name='home'),
    path('blank/',views.blank ),
    path('letter/new/',views.get_letter.as_view() , name='get_letter'),
    path('adminUsers/',views.adminUsers,name='adminUsers'),
    path('level/',views.level,name='level'),
    path('new_level/',views.new_level.as_view(),name='new_level'),
]