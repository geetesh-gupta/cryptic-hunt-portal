from django.views.generic import TemplateView
from question_answer.models import Question


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        question_list = Question.objects.filter(published=True)
        context['question_list'] = question_list
        return context
