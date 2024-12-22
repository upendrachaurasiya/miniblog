from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="Password Again Please",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password1","password2"]
        labels = {"email":"Email","first_name":"First Name","last_name":"Last Name"}
        widgets = {"username":forms.TextInput(attrs={"class":"form-control"}),
                   "email":forms.EmailInput(attrs={"class":"form-control"}),
                   "first_name":forms.TextInput(attrs={"class":"form-control","autofocus":True}),
                   "last_name":forms.TextInput(attrs={"class":"form-control"}),
                   }
        
class LoginForm(AuthenticationForm):
     username = UsernameField(widget=forms.TextInput(attrs={"class":"form-control","autofocus":True}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
     
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","desc"]
        labels = {"title":"Title","desc":"Description"}
        widgets = {"title":forms.TextInput(attrs={"class":"form-control"}),
       "desc":forms.Textarea(attrs={"class":"form-control"})
       }
       