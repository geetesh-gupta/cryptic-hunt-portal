from django.contrib import admin
from accounts.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    class Meta:
        model = UserProfile
        # All fields of Answer
        fields = '__all__'
