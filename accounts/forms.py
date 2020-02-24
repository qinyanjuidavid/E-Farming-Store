from django import forms
from django.forms import ModelForm
from accounts.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(ModelForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Password Confirmation",widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=('username','first_name','last_name','email')

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password don\'t match')
        return password2

    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model=User
        fields=('username','first_name','last_name','password','is_admin','is_staff','is_active')
    def clean_password(self):
        return self.initial['password']
class RegistrationForm(ModelForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Password Confirmation",widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=('first_name','last_name','email','username')

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password don\'t match')
        return password2

    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
class TestForm(ModelForm):
        password=ReadOnlyPasswordHashField()
        class Meta:
            model=User
            fields=('username','first_name','last_name','password','is_admin','is_staff','is_active')
        def clean_password(self):
            return self.initial['password']
