from django import forms

class QuestionForm(forms.Form):
    description = forms.CharField()
    level = forms.CharField()
    image = forms.FileField(label ='choose an image')
    answer = forms.CharField()

class AnswerForm(forms.Form):
	key = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'key-text'}))