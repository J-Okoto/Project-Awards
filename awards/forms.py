from django import forms
from .models import Profile,Rating



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['overall_score','profile','post']