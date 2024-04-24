from django import forms

from . models import Booking
from . models import Contact
# create your forms here

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name', 'class':'contact_form_name input_field'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'E-mail','class':'contact_form_email input_field'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject','class':'contact_form_subject input_field'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message','class':'text_field contact_form_message'}))

class BookingForm(forms.Form):
    destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'destination','class':'destination search_input'}))
    check_in = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'YYY-MM-DD', 'class':'check_in search_input'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'YYY-MM-DD', 'class':'check_out search_input'}))
    adults = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'number','class':'dropdown_item_select search_input'}))
    children = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'number', 'class':'dropdown_item_select search_input'}))