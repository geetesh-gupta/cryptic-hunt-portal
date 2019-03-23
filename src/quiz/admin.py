from django.contrib import admin
from .models import Quiz, QuestionOrder, UserQuizDetailsModel, UserQueAnsModel


class QuestionOrderInline(admin.TabularInline):
    model = QuestionOrder
    extra = 1


class UserQuizDetailsInline(admin.TabularInline):
    model = UserQuizDetailsModel
    extra = 1
    readonly_fields = ['user', 'quiz', 'score', 'cur_que_num', 'completed']


class UserQueAnsInline(admin.TabularInline):
    model = UserQueAnsModel
    extra = 1
    readonly_fields = ['user_quiz_details', 'question', 'answers']


# Register Quiz module on the admin interface
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    # Display customised list on admin page
    list_display = ['name', 'published']
    inlines = (QuestionOrderInline, UserQuizDetailsInline)

    class Meta:
        model = Quiz
        # All fields of Quiz
        fields = '__all__'


@admin.register(QuestionOrder)
class QuestionOrderAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'question', 'order']

    class Meta:
        model = QuestionOrder
        fields = '__all__'


@admin.register(UserQuizDetailsModel)
class UserQuizDetailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'cur_que_num', 'completed']
    readonly_fields = ['user', 'quiz', 'score', 'cur_que_num', 'completed']
    inlines = (UserQueAnsInline,)

    class Meta:
        model = UserQuizDetailsModel
        fields = '__all__'


@admin.register(UserQueAnsModel)
class UserQueAnsAdmin(admin.ModelAdmin):
    list_display = ['user_quiz_details', 'question', 'answers']
    readonly_fields = ['user_quiz_details', 'question', 'answers']

    class Meta:
        model = UserQueAnsModel
        fields = '__all__'
