from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class QuizCategory(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    about = RichTextUploadingField(null=True, blank=True, default='')
    date_published = models.DateTimeField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_published']
        verbose_name_plural = 'quiz categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(QuizCategory, self).save(*args, **kwargs)
