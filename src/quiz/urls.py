from django.urls import path
from quiz.views import IndexView, QuizView, ResultView

app_name = 'quiz'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/<int:num>/', QuizView.as_view(), name='quiz'),
    path('<slug:slug>/result/', ResultView.as_view(), name='result')
]
