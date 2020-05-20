from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    display_name = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)