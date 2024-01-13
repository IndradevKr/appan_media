from django.forms import ModelForm
from .models import ContactModel, Comment

class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        

   