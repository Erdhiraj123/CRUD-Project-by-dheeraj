from django import forms
from . models import User
from django.forms import ModelForm

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['studentname','email','password']
        widgets={
            'studentname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }

class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields=['teachername','email','password']
        widgets={
            'teachername':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
