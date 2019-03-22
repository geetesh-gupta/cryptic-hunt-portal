from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('quiz/', include('quiz.urls'))
]
