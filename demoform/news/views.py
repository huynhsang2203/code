from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.


class ClassIndex(View):
    def get(self, request):
        kq = '123'
        return HttpResponse(kq)


class ClassPost(View):
    def get(self, request):
        post = PostForm
        return render(request, 'news/add_news.html', {'post': post})


def post_view(request):
    if request.method == 'POST':
        context = PostForm(request.POST)
        if context.is_valid():
            context.save()
            return HttpResponse('Da luu')
        else:
            HttpResponse('Chua luu')
    else:
        HttpResponse('Khong co post request')


def email(request):
    send = SendEmail()
    return render(request, 'news/email.html', {'send': send})


def list_mail(request):
    if request.method == 'POST':
        context = SendEmail(request.POST)
        if context.is_valid():
            title_get = context.cleaned_data['title']
            content_get = context.cleaned_data['content']
            cc_get = context.cleaned_data['cc']
            email_get = context.cleaned_data['email']
            list = {'title_get': title_get, 'cc_get': cc_get,
                    'email_get': email_get, 'content_get': content_get}
            return render(request, 'news/list_mail.html', list)
        else:
            return HttpResponse('Khong co thong tin')
    else:
        return HttpResponse('Khong co thong tin gui')
