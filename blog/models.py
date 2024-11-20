from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default='', editable=False)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_category_url(self):
        kwargs = {
            "pk": self.id,
            'slug': self.slug,
        }
        return reverse("blog:category_page", kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Post(models.Model):
    STATUS_CHOICES = ( 
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    title = models.CharField(max_length=200)
    content = CKEditor5Field('Content', config_name='extends')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='category')
    thumbnail = models.ImageField(upload_to='post_img', blank=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, default='', editable=False)
    description = models.CharField(max_length=165, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='Draft')

    def __str__(self):
        return self.title

    def user(self):
        return self.author.user.username

    @property
    def thumbnail_url(self):
      try:
        url = self.thumbnail.url
      except:
        url = ''
      return url


    class Meta:
        ordering = ['-updated']

    def get_absolute_url(self):
        kwargs = {
            "pk": self.id,
            'slug': self.slug,
        }
        return reverse("blog:post_detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)