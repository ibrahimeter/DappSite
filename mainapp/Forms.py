from django import forms
from .models import Maintenance
from .models import AnnualReport

class MainForm(forms.ModelForm):
    class Meta :
        model = Maintenance
        fields = '__all__'

class annualrepForm(forms.ModelForm):
    class Meta :
        model = AnnualReport
        fields = '__all__'