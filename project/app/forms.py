from django import forms 
from . models import Players, UserPredictModel
from . models import Patient_info
from . models import Patient_info1


INPUT_CLASSES = 'mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md'

class Players_information_form(forms.ModelForm):

    class Meta:
        model = Players    
        fields = ['first_name','last_name','photo','date_of_birth','nationality','team', 'sports']
        widget = {
            
            'first_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES,
            }),
            'photo':forms.FileInput(attrs={
                'class':INPUT_CLASSES,
            }),
            
            'last_name':forms.TextInput(attrs={
                'class':INPUT_CLASSES,
            }),
            'date_of_birth':forms.DateInput(attrs={
                'class':INPUT_CLASSES,
            }),
            'nationality':forms.Select (attrs={
                'class':INPUT_CLASSES,
            }),
            'team':forms.Select(attrs={
                'class':INPUT_CLASSES,
            }),
            'Sports':forms.Select(attrs={
                'class':INPUT_CLASSES,
            }),
            
        }


from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


from . models import UserPredictModel




class UserPredictForm(forms.ModelForm):
    
    class Meta:
        model = UserPredictModel
        fields = ['image']


class Patient_info_Form(forms.ModelForm):
    class Meta:
        model = Patient_info
        fields = ['Country', 'CapStatus', 'Innings', 'Runs', 'Balls', 'Average', 'SR', 'Fifites', 'hundreds', 'Fours', 'Sixes', 'Notout', 'PlayerRole']


class Patient_info_Form1(forms.ModelForm):
    class Meta:
        model = Patient_info1
        fields = ['Specialism', 'Innings', 'Avg', 'SR', 'Fifties', 'Hundreds', 'Fours', 'Sixes', 'Runs', 'Balls', 'NotOuts']



    

