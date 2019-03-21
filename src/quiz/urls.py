from django.urls import path
from quiz.views import IndexView, QuizView

app_name = 'quiz'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/<int:num>/', QuizView.as_view(), name='quiz')
]
