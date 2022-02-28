from django.forms import ModelForm, TextInput, Textarea, FileInput, Select
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'photo']

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control mr-0 ml-auto",
                "placeholder": "Post title"
            }),
            "text": Textarea(attrs={
                "class": "form-control mr-0 ml-auto",
                "placeholder": "Post full-text"
            }),
            'photo': FileInput(attrs={
                'class': 'form-control mr-0 ml-auto',
            }),
            # 'author': Select(attrs={
            #     'class': 'form-select'
            # })
            
        }
