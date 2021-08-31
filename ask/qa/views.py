from django.http import HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.urls.base import reverse
from django.views.decorators.http import require_GET
from qa.forms import AnswerForm, AskForm, LoginForm, SignupForm
from qa.models import Question


def paginate(request, qs, baseurl):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    try:
        limit = int(request.GET.get('limit', 10))
        if limit > 10:
            limit = 10
    except ValueError:
        limit = 10
    paginator = Paginator(qs, limit)
    paginator.baseurl = baseurl
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator


@require_GET
def main(request, *args, **kwargs):
    qs_questions = Question.objects.new()
    baseurl= '/?page='
    page, paginator = paginate(request, qs_questions, baseurl)
    context = {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        'main_title': 'New Questions',
        'user': request.user,
    }
    return render(request, 'pagination.html', context)


@require_GET
def popular(request, *args, **kwargs):
    qs_questions = Question.objects.order_by('-rating')
    baseurl= '/popular/?page='
    page, paginator = paginate(request, qs_questions, baseurl)
    context = {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        'main_title': 'Popular Questions',
    }
    return render(request, 'pagination.html', context)


def question(request, **kwargs):
    question = get_object_or_404(Question, id=kwargs['question_id'])
    answers = question.answer_set.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else: # Request = 'GET'
        form = AnswerForm(initial={'question': question.id})
    context = {
        'user': request.user,
        'question': question,
        'answers': answers,
        'form': form,
    }
    return render(request, 'question.html', context)


def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else: # Request = 'GET'
        form = AskForm()
    context = { 'form': form }
    return render(request, 'ask.html', context)


def user_signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            url = request.POST.get('continue', '/')
            return HttpResponseRedirect('/')
    else: # Request = 'GET'
        form = SignupForm()
    context = { 'form': form }
    return render(request, 'signup.html', context)
    

def user_login(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.do_login()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('urls_home'))
            else:
                messages.error(request, 'Wrong username or password')
                return HttpResponseRedirect(reverse('urls_login'))
    else: # Request = 'GET'
        form = LoginForm()
    context = {
        'user': request.user,
        'form': form,
    }
    return render(request, 'login.html', context)


def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('urls_home'))


def test(request, *args, **kwargs):
    return HttpResponse('OK\n')



def new(request, *args, **kwargs):
    pass
