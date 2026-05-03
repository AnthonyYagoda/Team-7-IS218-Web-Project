from django import forms
from hello.models import Feedback


#Lab 3 Feedback Form Stuff:  
#Creates a Form based on Feedback that takes in the ratings and comments fields.
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['ratings', 'comments']