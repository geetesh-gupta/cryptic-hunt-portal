from django.contrib import admin
from social_django.models import Association, Nonce, UserSocialAuth
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('quiz/', include('quiz.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('auth/', include('social_django.urls', namespace='social')),
]

admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)
