from quiz.models import Quiz
from django.views.generic import TemplateView, ListView


class IndexView(ListView):
    model = Quiz
    template_name = 'quiz/index.html'
    context_object_name = 'quizzes'


class QuizView(TemplateView):
    template_name = 'quiz/quiz.html'

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        quiz = Quiz.objects.filter(published=True, slug=kwargs['slug']).all()[0]
        context['quiz'] = quiz
        return context
