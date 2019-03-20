from django.contrib import admin
from .models import Answer # Import Question and Answer modules


# Register Answer module on the admin interface
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = Answer
        # All fields of Answer
        fields = '__all__'
