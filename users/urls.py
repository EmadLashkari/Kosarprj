from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('add_user/',views.user_add , name='user_add'),
    path('profile/',views.profile , name='profile')
    
]

