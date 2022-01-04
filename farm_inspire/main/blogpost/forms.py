from django.forms import ModelForm
from accounts.models import User
from django.contrib.auth.forms import UserChangeForm


from .models import BlogPost,Comment,Feedback
from django import forms



class PostForm(forms.ModelForm):
      class Meta:
        model = BlogPost
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('name','body')


class feedBackForm(ModelForm):
  
    class Meta:
        model = Feedback
        fields = '__all__'

class EditProfile(UserChangeForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    date_joined=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','date_joined')