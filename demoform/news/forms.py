from django import forms
from django.db.models import fields
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'time_create',)


class SendEmail(forms.Form):
    title = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'huynhsang', 'id': 'noidung'}))
    cc = forms.BooleanField(required=False)
