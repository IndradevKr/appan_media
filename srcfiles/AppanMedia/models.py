from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class ContactModel(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return self.fullName


class userProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.PROTECT,)
    bio = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return self.user.get_username()

class blogPost(models.Model):
    class Meta:
        ordering = ["-published_date"]
    title = models.CharField(max_length=255, unique = True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=150, unique = True)
    image = models.ImageField(upload_to='images/', blank=True)
    content = RichTextField(blank=True, null = True)
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    published_status = models.BooleanField(default=False)

    author = models.ForeignKey(userProfile, on_delete= models.PROTECT)
    
class Comment(models.Model):
    post = models.ForeignKey(blogPost, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.name)

class Testimonial(models.Model):
    client_name = models.CharField(max_length=50)
    client_feedback = models.TextField()
    client_image = models.ImageField(upload_to='images/', blank=True)