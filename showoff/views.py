from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question


# def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'showoff/detail.html', {'question': question})
#
#
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'showoff/results.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'showoff/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'showoff/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'showoff/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'showoff/detail.html',
                      {'question': question,
                       'error_message': "请选一个选项", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('showoff:results',
                                            args=(question.id,)))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'showoff/index.html', context)


# def detail(request):
#   return HttpResponseRedirect(reverse('polls:index',
#        current_app = request.resolve  # r_match.namespace))
