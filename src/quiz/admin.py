from django.contrib import admin
from .models import Quiz, QuestionOrder, Score


class QuestionOrderInline(admin.TabularInline):
    model = QuestionOrder
    extra = 1


class ScoreInline(admin.TabularInline):
    model = Score
    extra = 1
    readonly_fields = ['user', 'score']


# Register Quiz module on the admin interface
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    # Display customised list on admin page
    list_display = ['name', 'published']
    inlines = (QuestionOrderInline, ScoreInline,)

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
