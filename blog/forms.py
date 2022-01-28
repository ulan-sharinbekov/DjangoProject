from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

## формы связанные с моделю
class AddPostForm(forms.ModelForm):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'content','photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'content': forms.Textarea(attrs={'cols':60, 'rowa':10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("Длина привышает 200 символов")
        return title

## формы не связанные с моделю
#class AddPostForm(forms.Form):
    #title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class':'form-input'}))
    #slug = forms.SlugField(max_length=255, label="URL")
    #content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}), label="Контент")
    #is_published = forms.BooleanField(label="Публикация", required=False, initial=True)
    #cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория", empty_label="Категория не выбрана")



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="логин", widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label="пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label="Е-mail", widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="логин", widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label="пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))




