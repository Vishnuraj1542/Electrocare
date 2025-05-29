from django import forms
from section_app.models import OfficeDetails

class OfficeForm(forms.ModelForm):
    class Meta:
        model=OfficeDetails
        fields = ['office_name', 'address', 'building_no', 'district', 'local_body']