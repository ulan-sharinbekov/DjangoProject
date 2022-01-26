from  django import forms

class NewForms(forms.Form):
    new_form = forms.CharField(label = 'New_atribut1',max_length=255)



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)