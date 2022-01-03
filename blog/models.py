from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    # character field : 글자 수가 제한된 텍스트를 정의할 때
    title = models.CharField(max_length=50)
    # text field : 글자 수의 제한이 없는 것
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title