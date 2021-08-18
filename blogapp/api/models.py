from django.db import models
from django.db.models.fields import SlugField

# Create your models here.

import string
import random

from django.utils.text import slugify


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))



class Blog(models.Model):
    title = models.CharField(max_length=200, null=False , blank=False)
    slug = models.SlugField(default=None)
    category = models.CharField(max_length=200 , null=True)
    media= models.ImageField(blank=True)
    post = models.TextField(blank=False)
    author = models.CharField(null=False , blank=False , max_length=200)
    date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
            super(Blog, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class Categories(models.Model):
    tags = models.CharField(null=False , blank=True , max_length=200)

    def __str__(self):
        return self.tags