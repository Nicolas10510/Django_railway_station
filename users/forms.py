from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Введите имя пользователя'}
    )
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Введите пароль'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите имя пользователя'
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите имя'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите фамилию'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Введите адрес эл. почты'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Введите пароль'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Подтвердите пароль'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите имя пользователя',
            'readonly': True
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите имя'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите фамилию'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Введите адрес эл. почты'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')