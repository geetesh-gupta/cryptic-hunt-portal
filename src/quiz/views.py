from django.views.generic import TemplateView
from quiz.models import Quiz


class IndexView(TemplateView):
    template_name = 'quiz/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        quizzes = Quiz.objects.filter(published=True)
        context['quizzes'] = quizzes
        return context


class QuizView(TemplateView):
    template_name = 'quiz/quiz.html'

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        quiz = Quiz.objects.filter(published=True, slug=kwargs['slug']).all()[0]
        context['quiz'] = quiz
        return context
