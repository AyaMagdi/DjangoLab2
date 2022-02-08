from django import forms
from djangolab.models import Myusers


class Insert_forms(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    password = forms.CharField(label='Password', max_length=30)
    intake_id = forms.CharField(label='intake_id', max_length=30)



class Insert_model_forms(forms.ModelForm):
    class Meta:
        fields = ("name", "password", "intake_id",)
        model = Myusers

class Update_forms(forms.Form):
    name = forms.CharField(label='Name to change', max_length=30)
    new_name = forms.CharField(label='New name', max_length=30)