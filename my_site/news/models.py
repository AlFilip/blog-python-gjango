from django.db import models
from django.urls import reverse_lazy, reverse


class News(models.Model):
    title = models.CharField(max_length=120, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True,
                                     verbose_name="Дата редактирования")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name="Фото",
                              blank=True)
    is_published = models.BooleanField(default=True,
                                       verbose_name="Опубликовано")
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 verbose_name='Категория')
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at', 'title']

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})


class Category(models.Model):
    title = models.CharField(max_length=80, db_index=True)
    
    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']
