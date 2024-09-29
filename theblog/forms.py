from django import forms
from theblog.models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('header_image', 'title', 'author', 'category', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Dynamically fetch categories and set them as choices
        choices = Category.objects.all().values_list('name', 'name')
        self.fields['category'].widget = forms.Select(choices=choices, attrs={'class': 'form-control'})


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'header_image', 'snippet', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        # Dynamically fetch categories and set them as choices
        choices = Category.objects.all().values_list('name', 'name')
        self.fields['category'].widget = forms.Select(choices=choices, attrs={'class': 'form-control'})
