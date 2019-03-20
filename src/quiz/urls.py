from django.urls import path
from quiz.views import IndexView

app_name = 'quiz'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
