from captcha.fields import CaptchaField
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = '__all__'