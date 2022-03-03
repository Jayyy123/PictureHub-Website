from django.forms import ModelForm
from .models import UserProfile,Socials,AddSocials
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'password1','password2','email','username']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','username', 'profile_picture', 'bio', 'description', 'email','social_links']

