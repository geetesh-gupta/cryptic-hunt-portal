from django.contrib import admin
from .models import Question, Answer # Import Question and Answer modules


# Register Question module on the admin interface
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'quiz_category', 'order']
    list_filter = ['quiz_category__name', 'order']
    class Meta:
        model = Question
        # All fields of Question
        fields = '__all__'


# Register Answer module on the admin interface
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = Answer
        # All fields of Answer
        fields = '__all__'
