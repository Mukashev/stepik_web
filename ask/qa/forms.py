from django import forms
from django.contrib.auth import authenticate
from django.forms.widgets import HiddenInput
from qa.models import Answer, Question
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if title == '':
            raise forms.ValidationError('Empty title', code='validation_error')
        return title

    def clean_text(self):
        text = self.cleaned_data['text'].strip()
        if text == '':
            raise forms.ValidationError('Empty text', code='validation_error')
        return text

    def save(self):
        if self._user.is_anonymous:
            self._user = None
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text'].strip()
        if text == '':
            raise forms.ValidationError('Empty text', code='validation_error')
        return text

    def clean_question(self):
        try:
            question_obj = Question.objects.get(id=self.cleaned_data['question'])
        except:
            raise forms.ValidationError('Question not found', code='validation_error')
        return question_obj

    def save(self):
        if self._user.is_anonymous:
            self._user = None      
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if username == '':
            raise forms.ValidationError('Empty username', code='validation_error')
        return username

    def clean_password(self):
        password = self.cleaned_data['password'].strip()
        if password == '':
            raise forms.ValidationError('Empty password', code='validation_error')
        return password

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if email == '':
            raise forms.ValidationError('Empty email', code='validation_error')
        return email

    def save(self):
        new_user = User.objects.create_user(**self.cleaned_data)
        # At this point, new_user is a User object that has
        # already been saved to the database.
        new_user.save()
        return new_user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if username == '':
            raise forms.ValidationError('Empty username', code='validation_error')
        return username

    def clean_password(self):
        password = self.cleaned_data['password'].strip()
        if password == '':
            raise forms.ValidationError('Empty password', code='validation_error')
        return password

    def do_login(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        return user
