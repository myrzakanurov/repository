from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Data(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    data_file = models.FileField(upload_to='documents/')
    upload_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('repo:detail', kwargs={'username': self.author.username, 'pk': self.pk})
