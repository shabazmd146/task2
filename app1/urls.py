from django.urls import path
from app1 import views

app_name = 'app1'


urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('set',views.set,name='set'),
    path('get',views.get,name='get'),
    path('delete',views.delete,name='delete')
]