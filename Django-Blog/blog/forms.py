from django import forms
from .models import Comment, Post
from django.contrib.auth import get_user_model

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
            widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    query = forms.CharField()

class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(
            widget=forms.HiddenInput,
            queryset=get_user_model().
            objects.all(),
            disabled=True,
            )

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'body', 'status', 'tags')
        widgets = {
                'status': forms.RadioSelect(choices=Post.STATUS_CHOICES),
                }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('author')
        super(PostForm, self).__init__(*args, **kwargs)

