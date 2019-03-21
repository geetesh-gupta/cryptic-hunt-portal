from django.contrib import admin
from .models import Quiz  # Import Quiz module
from .models import QuestionOrder  # Import Quiz module


class QuestionOrderInline(admin.TabularInline):
    model = QuestionOrder
    extra = 1


# Register Quiz module on the admin interface
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    # Display customised list on admin page
    list_display = ['name', 'published']
    inlines = (QuestionOrderInline,)

    class Meta:
        model = Quiz
        # All fields of Quiz
        fields = '__all__'


# Register Quiz module on the admin interface
@admin.register(QuestionOrder)
class QuestionOrderAdmin(admin.ModelAdmin):
    # Display customised list on admin page
    list_display = ['quiz', 'question', 'order']

    class Meta:
        model = QuestionOrder
        # All fields of Quiz
        fields = '__all__'
