from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=1000, verbose_name="Заголовок поста")
    text=models.TextField(max_length=1000, verbose_name="Текст поста")
    preview=models.ImageField(upload_to="contents/image")
    is_public=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    views_counter = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ['title']