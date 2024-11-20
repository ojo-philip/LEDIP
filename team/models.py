from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field




class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True)
    citation = CKEditor5Field('Citation', config_name='extends')
    thumbnail = models.ImageField(upload_to='post_img', blank=True)
    slug = models.SlugField(max_length=200, default='', editable=False)
    # description = models.CharField(max_length=165, blank=True, null=True)

    def __str__(self):
        return self.name

    def user(self):
        return self.author.user.username

    def get_team_url(self):
        kwargs = {
            "pk": self.id,
            'slug': self.slug,
        }
        return reverse("team:team_page", kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    @property
    def thumbnail_url(self):
      try:
        url = self.thumbnail.url
      except:
        url = ''
      return url