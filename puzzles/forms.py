from django import forms

class QuestionForm(forms.Form):
    description = forms.CharField()
    level = forms.CharField()
    image = forms.FileField(label ='choose an image')
    answer = forms.CharField()

class AnswerForm(forms.Form):
    answer = forms.CharField(required=True)