from django.db import models


# Create your models here.

class DateTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(DateTimeModel):
    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published'),
        ('rejects', 'rejected')
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)


class Comment(DateTimeModel):
    nick = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
