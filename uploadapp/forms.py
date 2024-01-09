from django import forms
from .models import Uploads, UploadFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model=UploadFile
        fields='__all__'
        
class UploadForm(forms.ModelForm):
    class Meta:
        model=Uploads
        fields='__all__'


