from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db.models import fields
from .models import *

class ResgisterForm(forms.ModelForm):
  class Meta:
    model = MarriageRegister
    fields = "__all__"

class UserRegistrationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','password1','password2']

class BrideNidForm(forms.ModelForm):
  class Meta:
    model = MarriageRegister
    fields = ['bridesNid']

class BrideBirthCertificateForm(forms.ModelForm):
  class Meta:
    model = MarriageRegister
    fields = ['bridesBirthCertificate']
class BridePassportForm(forms.ModelForm):
  class Meta:
    model = MarriageRegister
    fields = ['bridesPassport']
class GroomNidForm(forms.ModelForm):
  class Meta:
    model = MarriageRegister
    fields = ['groomsNid']
class GroomBirthCertificateForm(forms.ModelForm):
  class Meta:
    model = MarriageRegister
    fields = ['groomsBirthCertificate']
class GroomPassportForm(forms.ModelForm):
  class Meta:
    model = MarriageRegister
    fields = ['groomsPassport']