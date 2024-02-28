from django.core.exceptions import ValidationError
from typing import Any
from django import forms
from .models import MalibuModel, GentraModel, CobaltModel, NexiaModel, UserRegisterModel

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(max_length=128)
    confirm_password = forms.CharField(max_length=128)

    def save(self, commit: True) -> Any:
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data["confirm_password"]
        if password == confirm_password:
            user= super().save(commit=False)
            user.set_password(password)
            user.save()
        else:
            raise ValidationError ("Passwords don't match!")

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password and confirm_password and password != confirm_password:
    #         raise ValidationError("Passwords don't match!")

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
    #     return user

            
    class Meta:
        model = UserRegisterModel
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=56)
    password = forms.CharField(max_length=56)    

class MalibuCreateForm(forms.ModelForm):
    class Meta:
        model = MalibuModel
        fields = '__all__'

class GentraCreateForm(forms.ModelForm):
    class Meta:
        model = GentraModel
        fields = '__all__'


class CobaltCreateForm(forms.ModelForm):
    class Meta:
        model= CobaltModel
        fields = '__all__'


class NexiaCreateForm(forms.ModelForm):
    class Meta:
        model = NexiaModel
        fields = '__all__'