from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    feature_image = models.ImageField(upload_to='feature_images/')
    description = models.TextField()
    slug = models.SlugField(unique=True, editable=True)
    content = FroalaField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
