from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from theblog.models import Profile


class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','facebook_url','instagram_url','X_url','linkedin_url')
        
        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control',}),
            'profile_pic' : forms.FileInput(attrs={'class': 'form-control'}),
            'facebook_url' : forms.TextInput(attrs={'class':'form-control',}),
            'instagram_url' : forms.TextInput(attrs={'class':'form-control',}),
            'X_url' : forms.TextInput(attrs={'class':'form-control',}),
            'linkedin_url' : forms.TextInput(attrs={'class':'form-control',}),



        }

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'facebook_url', 'instagram_url', 'X_url', 'linkedin_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control'}),
            'X_url': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class Update_Password_Form(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your current password'}))
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}))

    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
        # Adding widgets to fields defined in the UserCreationForm (like username, password1, password2)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
        }

class Edit_Profile_Form(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

 
