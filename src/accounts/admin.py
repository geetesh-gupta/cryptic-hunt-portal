from django.contrib import admin
from accounts.models import UserProfile
from quiz.admin import UserQuizDetailsInline


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    inlines = (UserQuizDetailsInline,)

    class Meta:
        model = UserProfile
        # All fields of Answer
        fields = '__all__'
