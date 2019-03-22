from django.views.generic import ListView, UpdateView, DetailView
from quiz.models import Quiz, QuestionOrder
from .forms import AnswerForm
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin


class AccessMixin(LoginRequiredMixin):
    template = 'error.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return render(request, self.template, {'error': 'Admins are not allowed to fill the quiz. Contact admin.',
                                                   'redirect_url': '/admin/', 'label': 'Go To Admin'})
        return super().dispatch(request, *args, **kwargs)


class IndexView(ListView):
    model = Quiz
    template_name = 'quiz/index.html'
    context_object_name = 'quizzes'


class QuizView(AccessMixin, UpdateView):
    template_name = 'quiz/quiz.html'
    context_object_name = 'quiz'
    form_class = AnswerForm

    def form_valid(self, form):
        num_of_que = self.get_quiz(self.kwargs['slug']).questions.count()
        if (self.kwargs['num'] < num_of_que):
            form.instance.current_question = self.kwargs['num'] + 1
        else:
            form.instance.current_question = 1
        return super().form_valid(form)

    def get_queryset(self):
        quiz = Quiz.objects.filter(published=True, slug=self.kwargs['slug'])
        return quiz

    def get_success_url(self):
        num_of_que = self.get_quiz(self.kwargs['slug']).questions.count()
        if (self.kwargs['num'] < num_of_que):
            return reverse('quiz:quiz', kwargs={'slug': self.kwargs['slug'], 'num': self.kwargs['num'] + 1})
        else:
            return reverse('quiz:result', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        quiz = self.get_quiz(self.kwargs['slug'])
        cur_que_num = self.kwargs['num']
        cur_que = QuestionOrder.objects.filter(quiz=quiz, order=cur_que_num)[0].question
        context = super(QuizView, self).get_context_data(**kwargs)
        context['current_question'] = cur_que
        return context

    def dispatch(self, request, *args, **kwargs):
        cur_que_num = self.get_quiz(self.kwargs['slug']).current_question
        if kwargs['num'] != cur_que_num:
            return redirect(reverse('quiz:quiz', kwargs={'slug': kwargs['slug'], 'num': cur_que_num}))
        else:
            return super(QuizView, self).dispatch(request, *args, **kwargs)

    def get_quiz(self, slug):
        return Quiz.objects.filter(published=True, slug=slug)[0]


class ResultView(AccessMixin, DetailView):
    template_name = 'quiz/result.html'
    context_object_name = 'result'

    def get_queryset(self):
        quiz = Quiz.objects.filter(published=True, slug=self.kwargs['slug'])
        return quiz
