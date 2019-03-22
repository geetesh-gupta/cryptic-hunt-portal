from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('quiz/', include('quiz.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
]
