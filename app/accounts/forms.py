from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import PasswordChangeForm

from .models import User

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': '+998997980727'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


class UserCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'Last Name'}), required=True)
    username = forms.CharField(widget=TextInput(attrs={'placeholder': '+998997980727'}), required=True)
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}), required=True)
    confirm_password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Confirm Password'}), required=True)



    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

    def clean_username(self):
        username = self.cleaned_data['username']
        # Check if the username is already in use
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu telefon raqam bilan foydalanuvchi ro'yxatdan o'tgan")

        return username
    def clean_confirm_password(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError("Ikkala parolingiz ham bir-biriga teng bo'lishi kerak!")
        return data['confirm_password']
    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['confirm_password'])
        user.save()

        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'photo')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        strip=False
    )
    new_password1 = forms.CharField(
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False
    )