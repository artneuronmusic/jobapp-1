from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

#modern form
class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        #exclude=('first_name')
        labels={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter email')

        }
        # help_texts={
        #     'first_name':_("Enter characters only")
        # },  #use forms.as_p  in html
        error_messages={
            'first_name':{
                'required':_('first name is required'),
            },
        }
# def validate_comma(value):
#         if ',' in value:
#             raise forms.ValidationError("Invalid last name")
#         return value
# class SubscribeForm(forms.Form):
#     first_name=forms.CharField(max_length=100, validators=[validate_comma], label="Enter first name")
#     last_name=forms.CharField(max_length=100, disabled=False, validators=[validate_comma], label="Enter last name")
#     email=forms.EmailField(max_length=100, required=False, label="Enter email", help_text="Enter characters only")

#     # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if ',' in data:
    #         raise forms.ValidationError("Invalid first name")
    #     return data
