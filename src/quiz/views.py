from django.views.generic import ListView, UpdateView
from quiz.models import Quiz, QuestionOrder
from .forms import AnswerForm
from django.urls import reverse


class IndexView(ListView):
    model = Quiz
    template_name = 'quiz/index.html'
    context_object_name = 'quizzes'


class QuizView(UpdateView):
    template_name = 'quiz/quiz.html'
    context_object_name = 'quiz'
    form_class = AnswerForm

    def form_valid(self, form):
        form.instance.current_question = self.kwargs['num'] + 1
        form.check_correct_answer()
        return super().form_valid(form)

    def get_queryset(self):
        quiz = Quiz.objects.filter(published=True, slug=self.kwargs['slug']).all()
        return quiz

    def get_success_url(self):
        return reverse('quiz:quiz', kwargs={'slug': self.kwargs['slug'], 'num': self.kwargs['num'] + 1})

    def get_context_data(self, **kwargs):
        quiz = Quiz.objects.filter(published=True, slug=self.kwargs['slug']).all()[0]
        cur_que_num = self.kwargs['num']
        cur_que = QuestionOrder.objects.all().filter(quiz=quiz, order=cur_que_num)[0].question
        context = super(QuizView, self).get_context_data(**kwargs)
        context['current_question'] = cur_que
        return context
