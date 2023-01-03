from django.urls import path
from app2 import views

app_name='app2'

urlpatterns = [
    path('setsession',views.setsession,name='session'),
    path('getsession',views.getsession,name='session'),
    path('delsession',views.delsession,name='session')
]