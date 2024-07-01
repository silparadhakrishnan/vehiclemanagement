from django import forms
from django.contrib.auth.models import User
from vehicleapp.models import VehicleModel



class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=VehicleModel
        fields=["first_name","last_name","email","username","password","vehiclename","price"]
        
class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        
        
    
    
        
        
        
        