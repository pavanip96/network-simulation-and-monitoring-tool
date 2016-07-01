from django import forms
from .models import FileModel ,EventModel
from django.forms import extras
from django.forms import ModelForm
from django.db.models.fields import DateField, DateTimeField
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.admin import widgets
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import AuthenticationForm
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
 
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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_valid():
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

    
class CaptureForm(forms.Form):
    Time= forms.CharField(max_length=30,widget=forms.RadioSelect(choices=(('5','5'),('10','10'))))
    file = forms.FileField(label='Select a CSV(upload) file')
    
class idForm(forms.Form):
    id1=forms.IntegerField()
    
class SimulateForm(forms.Form):
    Packets_loss=forms.IntegerField()
    Jitter=forms.IntegerField()
    Latency=forms.IntegerField()


class FileForm(forms.Form):
    file = forms.FileField(label='Select a CSV(upload) file')
    file2 = forms.FileField(label='Select a CSV(download) file')

class EventForm(forms.Form):
    
    first_name = forms.CharField(max_length=30)
    event_description = forms.CharField(max_length=200)
    startdate = forms.DateField(localize=True,input_formats=settings.DATE_INPUT_FORMATS)
    
   
    fields='__all__'

    def __str__(self):
          return self.event_description
        
class SearchForm(forms.Form):

    startdate = forms.DateField(localize=True,input_formats=settings.DATE_INPUT_FORMATS,widget=SelectDateWidget)
    enddate=forms.DateField(localize=True,input_formats=settings.DATE_INPUT_FORMATS)

    
    fields='__all__'
