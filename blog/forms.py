from django import forms

from blog import models


class CommentForm(forms.ModelForm):
    """Comment form"""
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': '5',
    }))

    class Meta:
        model = models.Comment
        fields = [
            'text',
        ]
