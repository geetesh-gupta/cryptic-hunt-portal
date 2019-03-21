from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from question_answer.models import Question


class Quiz(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    about = RichTextUploadingField(null=True, blank=True, default='')
    date_published = models.DateTimeField()
    questions = models.ManyToManyField(Question, related_name='quiz')
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
