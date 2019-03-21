from django.contrib import admin
from .models import Question, Answer  # Import Question and Answer modules


# Register Question module on the admin interface
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # Display customised list on admin page
    list_display = ['Questions', 'slug', 'Quizzes', 'Order']
    # Add filters on admin page
    list_filter = ['quiz__name']

    class Meta:
        model = Question
        # All fields of Question
        fields = '__all__'

    # list_display for questions
    def Questions(self, obj):
        question = (obj.question[3:47] + '...') if len(obj.question) > 50 else obj.question[3:-4]
        return question

    # list_display for quizzes as comma-separated-list
    def Quizzes(self, obj):
        return ", ".join([
            quiz.name for quiz in obj.quiz.all()
        ])

    # list_display for question_orders as comma-separated-list
    def Order(self, obj):
        return ", ".join([
            str(que.order) for que in obj.questionorder_set.all()
        ])


# Register Answer module on the admin interface
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    # Display customised list on admin page
    list_display = ['Answers', 'Questions', 'Quizzes']
    # Add filters on admin page
    list_filter = ['questions__quiz__name', 'questions__slug']

    class Meta:
        model = Answer
        # All fields of Answer
        fields = '__all__'

    # list_display for answers
    def Answers(self, obj):
        return obj.name

    # list_display for questions as comma-separated-list
    def Questions(self, obj):
        return ", ".join([
            que.slug[:20] for que in obj.questions.all()
        ])

    # list_display for question_orders as comma-separated-list
    def Quizzes(self, obj):
        quizzess = ''
        for question in obj.questions.all():
            quizzess = ", ".join([
                str(each.quiz.name) for each in question.questionorder_set.all()
            ])

        return quizzess
