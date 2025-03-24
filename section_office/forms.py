from django import forms
from .models import OfficeDetails

class OfficeForm(forms.ModelForm):
    class Meta:
        model=OfficeDetails
        fields = ['office_name', 'address', 'building_no', 'district', 'local_body']