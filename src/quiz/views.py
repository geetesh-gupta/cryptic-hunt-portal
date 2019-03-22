from django.views.generic import ListView, UpdateView, DetailView
from quiz.models import Quiz, QuestionOrder
from .forms import AnswerForm
from django.urls import reverse


class IndexView(ListView):
    model = Quiz
    template_name = 'quiz/index.html'
    context_object_name = 'quizzes'


class QuizView(UpdateView):
    # http_method_names = ['post']
    template_name = 'quiz/quiz.html'
    context_object_name = 'quiz'
    form_class = AnswerForm

    def form_valid(self, form):
        num_of_que = Quiz.objects.all().filter(slug=self.kwargs['slug'])[0].questions.all().count()
        if (self.kwargs['num'] < num_of_que):
            form.instance.current_question = self.kwargs['num'] + 1
        else:
            form.instance.current_question = 1
        return super().form_valid(form)

    def get_queryset(self):
        quiz = Quiz.objects.filter(published=True, slug=self.kwargs['slug']).all()
        return quiz

    def get_success_url(self):
        num_of_que = Quiz.objects.all().filter(slug=self.kwargs['slug'])[0].questions.all().count()
        if (self.kwargs['num'] < num_of_que):
            return reverse('quiz:quiz', kwargs={'slug': self.kwargs['slug'], 'num': self.kwargs['num'] + 1})
        else:
            return reverse('quiz:result', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        quiz = Quiz.objects.filter(published=True, slug=self.kwargs['slug']).all()[0]
        cur_que_num = self.kwargs['num']
        cur_que = QuestionOrder.objects.all().filter(quiz=quiz, order=cur_que_num)[0].question
        context = super(QuizView, self).get_context_data(**kwargs)
        context['current_question'] = cur_que
        return context


class ResultView(DetailView):
    template_name = 'quiz/result.html'
    context_object_name = 'result'

    def get_queryset(self):
        quiz = Quiz.objects.filter(published=True, slug=self.kwargs['slug']).all()
        return quiz
