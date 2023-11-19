from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from vpn.models import Site, Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')


class SiteForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ("site_name", "site_url")
        exclude = ['user']


class SiteSearchForm(forms.Form):
    site_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by site name"})
    )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
