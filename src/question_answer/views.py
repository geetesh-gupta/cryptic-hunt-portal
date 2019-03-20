from django.views.generic import TemplateView
from quiz.models import Quiz


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        quiz = Quiz.objects.filter(published=True)
        context['quiz'] = quiz
        return context
