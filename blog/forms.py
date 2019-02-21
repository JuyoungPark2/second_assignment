from django import forms
from .models import Blog
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields
from .models import summer_note


class BlogPost(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'body')
        widgets = {
            'body': SummernoteWidget(),
        }
