from django.db import models
import datetime
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField(max_length=150)
    article_text = models.TextField()
    image = models.ImageField()
    article_autor = models.CharField(max_length=55)
    pub_data = models.DateTimeField()
    image = models.ImageField(
        upload_to='media/', blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_data >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor_name = models.CharField(max_length=55)
    comments_text = models.CharField(max_length=200)

    def __str__(self):
        return self.autor_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class File(models.Model):
    xml = models.FileField(upload_to='media/xml')