from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Attribute(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    description = RichTextUploadingField(null=True, blank=True)


    def __str__(self):
        return self.title


class Variations(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='variations', null=True, blank=True)
    attribute = models.ForeignKey(Attribute, null=True, on_delete=models.SET_NULL, related_name='variation')

    def __str__(self):
        return self.title
    