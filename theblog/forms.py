from django import forms
from theblog.models import Post,Category 

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for i in choices:
    choice_list.append(i)#

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('header_image','title','author','category','body','snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control',}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            'header_image' : forms.FileInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control',}),
            'body' : forms.Textarea(attrs={'class':'form-control',}),
            'snippet' : forms.Textarea(attrs={'class':'form-control',}),


        } 

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','header_image','snippet','category')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control',}),
            'body' : forms.Textarea(attrs={'class':'form-control',}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control',}),
            'snippet' : forms.Textarea(attrs={'class':'form-control',}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),


        }


