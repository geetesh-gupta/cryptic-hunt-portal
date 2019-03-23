from django.views.generic import ListView, UpdateView, DetailView
from quiz.models import Quiz, QuestionOrder, UserQuizDetailsModel, UserQueAnsModel
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


class IndexView(AccessMixin, ListView):
    model = Quiz
    template_name = 'quiz/index.html'
    context_object_name = 'quizzes'


class QuizView(AccessMixin, UpdateView):
    template_name = 'quiz/quiz.html'
    context_object_name = 'quiz'
    form_class = AnswerForm
    quiz = None
    quiz_slug = None
    cur_que = None
    user_quiz_details = None

    def form_valid(self, form):
        score = self.user_quiz_details.score
        if score == 0:
            self.user_quiz_details.score = 1
        else:
            self.user_quiz_details.score += 1

        if (self.kwargs['num'] < self.quiz.questions.count()):
            self.user_quiz_details.cur_que_num += 1
        else:
            self.user_quiz_details.completed = True
        self.user_quiz_details.save()
        return super().form_valid(form)

    def get_queryset(self):
        quiz = Quiz.objects.filter(published=True, slug=self.quiz_slug)
        return quiz

    def get_success_url(self):
        if self.user_quiz_details.completed:
            return reverse('quiz:result', kwargs={'slug': self.quiz_slug})
        else:
            return reverse('quiz:quiz', kwargs={'slug': self.quiz_slug, 'num': self.kwargs['num'] + 1})

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        context['current_question'] = self.cur_que
        return context

    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user.user
        self.quiz_slug = self.kwargs['slug']
        self.quiz = Quiz.objects.filter(published=True, slug=self.quiz_slug)[0]
        if not self.quiz.userquizdetailsmodel_set.filter(user=self.user).exists():
            self.user_quiz_details = UserQuizDetailsModel(user=self.user, quiz=self.quiz)
        else:
            self.user_quiz_details = self.quiz.userquizdetailsmodel_set.filter(user=self.user)[0]
        self.cur_que_num = self.user_quiz_details.cur_que_num
        self.cur_que = QuestionOrder.objects.filter(quiz=self.quiz, order=self.cur_que_num)[0].question
        completed = self.user_quiz_details.completed

        if completed:
            return redirect(reverse('quiz:result', kwargs={'slug': self.quiz_slug}))
        elif kwargs['num'] != self.cur_que_num:
            return redirect(reverse('quiz:quiz', kwargs={'slug': self.quiz_slug, 'num': self.cur_que_num}))
        else:
            return super(QuizView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(QuizView, self).get_form_kwargs()
        kwargs.update({'cur_que_num': self.quiz.questions.count()})
        return kwargs


class ResultView(AccessMixin, DetailView):
    template_name = 'quiz/result.html'
    context_object_name = 'result'

    def get_queryset(self):
        quiz = Quiz.objects.filter(published=True, slug=self.kwargs['slug'])
        return quiz

    def get_context_data(self, **kwargs):
        quiz = Quiz.objects.filter(published=True, slug=self.kwargs['slug'])[0]
        num_of_que = quiz.questions.count()
        score = UserQuizDetailsModel.objects.filter(user=self.request.user.user, quiz=quiz)[0].score
        context = super(ResultView, self).get_context_data(**kwargs)
        context['quiz'] = quiz
        context['num_of_que'] = num_of_que
        context['score'] = score
        return context
