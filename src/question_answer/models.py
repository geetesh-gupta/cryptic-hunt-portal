from django.db import models
from versatileimagefield.fields import VersatileImageField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Answer(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = RichTextUploadingField(null=True, blank=False, default='')
    slug = models.SlugField(unique=True)
    image = VersatileImageField(upload_to='images', null=True, blank=True)
    answers = models.ManyToManyField('Answer', related_name='questions')
    order = models.IntegerField(default=0, blank=False)
    custom_html_upper = models.TextField(null=True, blank=True, default='')
    custom_html_lower = models.TextField(null=True, blank=True, default='')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(Question, self).save(*args, **kwargs)
