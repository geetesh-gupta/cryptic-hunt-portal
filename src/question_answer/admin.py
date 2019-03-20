from django.contrib import admin
from .models import Question, Answer  # Import Question and Answer modules


# Register Question module on the admin interface
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['Questions', 'Quizzes', 'order']
    list_filter = ['quiz__name', 'order']

    class Meta:
        model = Question
        # All fields of Question
        fields = '__all__'

    def Quizzes(self, obj):
        return ", ".join([
            quiz.name for quiz in obj.quiz.all()
        ])

    def Questions(self, obj):
        return obj.question[3:-4]


# Register Answer module on the admin interface
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['Answers', 'Questions', 'Question_Orders']
    list_filter = ['questions__quiz__name', 'questions__order']

    class Meta:
        model = Answer
        # All fields of Answer
        fields = '__all__'

    def Answers(self, obj):
        return obj.name

    def Questions(self, obj):
        return ", ".join([
            que.slug for que in obj.questions.all()
        ])

    def Question_Orders(self, obj):
        return ", ".join([
            str(que.order) for que in obj.questions.all()
        ])
