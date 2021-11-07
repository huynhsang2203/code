from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Question

# Create your views here.


def index(request):
    taisan = ['dien thoai', 'tui sach', 'may tinh', ]
    myname = 'Huynh Sang'
    context = {'name': myname, 'taisan': taisan}
    return render(request, "./polls/index.html", context)


def detail(request, question_id):
    return HttpResponse("Ban dang xem cau hoi thu: %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Ban dang vote cau hoi thu %s" % question_id)


def question_list(request):
    list_question = Question.objects.all()
    context = {'list': list_question}
    return render(request, "./polls/question_list.html", context)


def detail_list_question(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "./polls/detail_list_question.html", {"qs": q})


def total_vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST['choice']
        c = q.choice_set.get(pk=data)
    except:
        HttpResponse('Khong co cau tra loi')
    c.vote = c.vote + 1
    c.save()
    return render(request,'./polls/total_vote.html',{'qs':q})
