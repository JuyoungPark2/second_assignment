from django import forms
from .models import Blog


class BlogPost(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'body']

    # title = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'title-input'}))
    # body = forms.CharField(widget=forms.Textarea(
    #     attrs={'class': 'body-input'}))
