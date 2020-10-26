from django import forms
from .models import Profile,Post,Rating

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['username','post_date','design','usability','creativity','content','overall_score','avatar',]
        widgets={
        
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['overall_score','profile','post']