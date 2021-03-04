from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200, verbose_name="Катерогия")
    slug = models.SlugField(max_length=80, verbose_name="Вид ссылки на категорию")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category',)

    def __str__(self):
        return self.category


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Загловок")
    text = models.TextField(verbose_name="Текст")
    quote = models.CharField(max_length=250, verbose_name="Цитата")
    slug = models.SlugField(max_length=80, verbose_name="Вид ссылки")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.PROTECT,
                                 verbose_name="Категория")
    photo = models.ImageField(upload_to="photo/%Y/%m", verbose_name="Фото")
    publish = models.BooleanField(verbose_name="Публиковано")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('create_date',)

    def __str__(self):
        return self.title