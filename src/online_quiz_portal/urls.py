from django.contrib import admin
from django.urls import path, include
from question_answer.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
