from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


#create your forms here
class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email',]
        label = {'email':'Email'}
