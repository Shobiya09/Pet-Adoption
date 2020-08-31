from django import forms
from web_app.models import Detail
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
class DetailForm(forms.ModelForm):

    class Meta:
        model=Detail
        fields=('name','phone_no','address','email','description','status','pet_type','pet_name')
