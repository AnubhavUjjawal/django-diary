from django.contrib.auth.models import User
from django.forms import ModelForm,PasswordInput
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password','first_name','last_name')

    def __init__(self, *args, **kwargs):
            # first call the 'real' __init__()
        super(UserForm, self).__init__(*args, **kwargs)
            # then do extra stuff:
        self.fields['username'].help_text = ''
        self.fields['password'].widget = PasswordInput(attrs={'placeholder': ''})
        self.fields['password'].widget.attrs['class'] = 'form-control'

class PostForm(ModelForm):

    class Meta:
        model = Posts
        fields = ('post_title','post_body')