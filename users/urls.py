from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('add_user/<int:id>',views.AddUser.as_view() , name='user_add'),
    path('profile/<int:id>',views.Profile.as_view() , name='profile')
    
]

