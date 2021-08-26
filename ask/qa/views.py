from django.core import paginator
from django.db.models.query_utils import Q
from qa.models import Question
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.core.paginator import EmptyPage, Paginator
from django.core.exceptions import ObjectDoesNotExist

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

def question(request, **kwargs):
    q = get_object_or_404(Question, id=kwargs['question_id'])
    # try:
    #     q = Question.objects.get(pk=kwargs['question_id'])
    # except (ObjectDoesNotExist, ValueError):
    #     raise Http404
    a = q.answer_set.all()
    context = {
        'question': q,
        'answers': a,
    }
    return render(request, 'question.html', context)

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

def ask(request, *args, **kwargs):
    pass

def new(request, *args, **kwargs):
    pass
