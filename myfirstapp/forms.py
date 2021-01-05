from django import forms


class FeedbackForm(forms.Form):
    Email=forms.CharField(label='Email',max_length=200, widget=forms.EmailInput())
    Password=forms.CharField(label='Password',max_length=200, widget=forms.PasswordInput)
