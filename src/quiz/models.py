from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from question_answer.models import Question
from accounts.models import UserProfile
from django.utils.timezone import now


class Quiz(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    about = RichTextUploadingField(null=True, blank=True, default='')
    date_published = models.DateTimeField(default=now)
    questions = models.ManyToManyField(Question, related_name='quiz', through='QuestionOrder')
    user = models.ManyToManyField(UserProfile, related_name='quiz', through='UserQuizDetailsModel')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_published']
        verbose_name_plural = 'quizzes'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Quiz, self).save(*args, **kwargs)


class QuestionOrder(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    order = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Order of Questions'
        verbose_name_plural = 'Order of Questions'


class UserQuizDetailsModel(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    cur_que_num = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.quiz.slug + '-' + self.user.user.username

    class Meta:
        verbose_name = "User's Quiz Details"
        verbose_name_plural = "User's Quiz Details"


class UserQueAnsModel(models.Model):
    user_quiz_details = models.ForeignKey(UserQuizDetailsModel, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.TextField()

    def __str__(self):
        return self.user_quiz_details.quiz.slug + '-' + self.user_quiz_details.user.user.username

    class Meta:
        verbose_name = "User's Question Answers"
        verbose_name_plural = "User's Question Answers"
