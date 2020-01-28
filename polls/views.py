from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):     
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()       
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


from django.shortcuts import HttpResponse
import time
import django.dispatch
from django.dispatch import receiver

work_done = django.dispatch.Signal(providing_args=['path', 'time'])

def send_signal(request):
    url_path = request.path
    print("Work has already been done, I will send a Signal")

    work_done.send(send_signal, path=url_path, time=time.strftime("%Y-%m-%d %H:%M:%S"))
    return HttpResponse("200,ok")

@receiver(work_done, sender=send_signal)
def my_callback(sender, **kwargs):
    print("I receive a signal from %s at %s, the url is %s" % (sender, kwargs['time'], kwargs["path"]))


from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def send_messages(request):
    messages.debug(request, 'debug:hello world!')
    messages.info(request, 'info:hello world!')
    messages.success(request, 'success:hello world!')
    messages.warning(request, 'warning:hello world!')
    messages.error(request, 'error:hello world!')
    return render(request, 'polls/show_messages.html')
    pass

def send_a_mail(request):
    email_title = '邮件标题'
    email_body = '邮件内容'
    emailfrom = settings.EMAIL_FROM
    emailto = 'li_min_sheng@qq.com'
    send_status = send_mail(email_title, email_body, emailfrom, [emailto])
    return HttpResponse('a mail was send from %s to %s.' % (emailfrom, emailto))
    pass

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginator_result(request):
    question_list = Question.objects.all()
    paginator = Paginator(question_list, 2)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        questions = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        questions = paginator.page(paginator.num_pages)
    return render(request, 'polls/paginator_result.html', {'questions': questions})


class paginatorView(generic.ListView):
    model = Question
    template_name = "polls/paginator_result_view.html"
    context_object_name = "questions"
    paginate_by = 2