#files.py
import re
from django import forms
from polls.models import property
from django.contrib.auth.models import User
from polls.models import UserAvatar
from django.utils.translation import ugettext_lazy as _

class PropRegistrationForm(forms.Form):

    Name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Property Name"))
    Price = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Price"))
    Location = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Location"))
    Lat = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, value = 38.388656)), label=_("Latitude"))
    Long= forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, value = -75.063863)), label=_("Longitude"))
    Owner = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Owner"))
    Description = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=256)), label=_("Description"))
    Image = forms.ImageField()
    def clean_username(self):
        try:
            prop = property.objects.get_or_create(Name__iexact=self.cleaned_data['Name'])
        except prop.DoesNotExist:
            return self.cleaned_data['Name']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    #def clean(self):
    #    if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
    #        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
 #               raise forms.ValidationError(_("The two password fields did not match."))
  #      return self.cleaned_data
class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    avatar = forms.ImageField(required = False)

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
