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
    custom_html_upper = models.TextField(null=True, blank=True, default='')
    custom_html_lower = models.TextField(null=True, blank=True, default='')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.question[3:-4]

    class Meta:
        ordering = ['slug']

    def _get_unique_slug(self):
        slug = slugify(self.question)[0:48]
        unique_slug = slug
        num = 1
        while Question.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
