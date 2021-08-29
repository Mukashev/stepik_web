from django.http.response import HttpResponseRedirect
from qa.forms import AnswerForm, AskForm
from qa.models import Question
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.core.paginator import EmptyPage, Paginator


# Create your views here.
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


def main(request, *args, **kwargs):
    qs_questions = Question.objects.new()
    baseurl= '/?page='
    page, paginator = paginate(request, qs_questions, baseurl)
    context = {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        'main_title': 'New Questions',
    }
    return render(request, 'pagination.html', context)


def question(request, **kwargs):
    question = get_object_or_404(Question, id=kwargs['question_id'])
    answers = question.answer_set.all()
    if request.method == 'POST':
        form = AnswerForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else: # Request = 'GET'
        form = AnswerForm(request.user, initial={'question_id': question.id})
    context = {
        'question': question,
        'answers': answers,
        'form': form,
    }
    return render(request, 'question.html', context)


def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.user, request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else: # Request = 'GET'
        form = AskForm(request.user)
    context = { 'form': form }
    return render(request, 'ask.html', context)


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


def test(request, *args, **kwargs):
    return HttpResponse('OK\n')

def login(request, *args, **kwargs):
    pass

def signup(request, *args, **kwargs):
    pass

def new(request, *args, **kwargs):
    pass
