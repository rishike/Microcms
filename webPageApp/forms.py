from django import forms
from webPageApp.models import WalkIn

class LeadCaptureForm(forms.Form):
    name = forms.CharField(max_length=255, widget= forms.TextInput (attrs={'class':'form-control mb-2'}))
    phone_number = forms.CharField(max_length=20, widget= forms.TextInput (attrs={'class':'form-control mb-2'}))
    email = forms.EmailField(widget= forms.EmailInput (attrs={'class':'form-control mb-2'}))
    address = forms.CharField(max_length=255, widget= forms.TextInput (attrs={'class':'form-control mb-2'}))
    city = forms.CharField(max_length=255, widget= forms.TextInput (attrs={'class':'form-control mb-2'}))
    country = forms.CharField(max_length=255, widget= forms.TextInput (attrs={'class':'form-control mb-2'}))
    referral_code = forms.CharField(max_length=10, widget= forms.TextInput (attrs={'class':'form-control mb-2'}))


class WalkInForm(forms.ModelForm):
    class Meta:
        model = WalkIn
        fields = ('lead', 'vendor', 'device', 'currency', 'offer_price', 'walkin_datetime')