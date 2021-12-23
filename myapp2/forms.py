from django import forms

from .models import Footballer, Club

class addClubForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Club
        fields  = '__all__'


class addFootballerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Footballer
        fields = '__all__'