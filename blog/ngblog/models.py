from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title    = models.CharField(max_length=150)
    image    = models.ImageField(upload_to='image', blank=True, null=True)
    body     = RichTextUploadingField(blank=True, null=True)
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # body     = models.TextField()
    post_id  = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug     = models.SlugField(allow_unicode=True, unique=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
    
    
class Category(models.Model):
    title = models.CharField(max_length=20)
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = models.SlugField(allow_unicode=True)
    
    def __str__(self) -> str:
        return self.title