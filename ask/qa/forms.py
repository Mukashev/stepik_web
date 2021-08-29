from django import forms
from django.forms.widgets import HiddenInput
from qa.models import Answer, Question
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, AnonymousUser


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    # def __init__(self, user, *args, **kwargs):
    #     if user.is_anonymous:
    #         self._user = None
    #     else:
    #         self._user = user
    #     super(AskForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title == '':
            raise forms.ValidationError('Empty title', code='validation_error')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == '':
            raise forms.ValidationError('Empty text', code='validation_error')
        return text

    def save(self):
        if self._user.is_anonymous():
            self._user = None
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    # def __init__(self, user, *args, **kwargs):
    #     if user.is_anonymous:
    #         self._user = None
    #     else:
    #         self._user = user
    #     super(AnswerForm, self).__init__(*args, **kwargs)

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == '':
            raise forms.ValidationError('Empty text', code='validation_error')
        return text

    def clean_question(self):
        try:
            question = Question.objects.get(id=self.cleaned_data['question'])
        except:
            raise forms.ValidationError('Question not found', code='validation_error')
        return question

    def save(self):
        self.cleaned_data['question'] = Question.objects.get(id=self.cleaned_data['question'])
        if self._user.is_anonymous():
            self._user = None      
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer