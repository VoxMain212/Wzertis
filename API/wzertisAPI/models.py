from django.db import models

# Create your models here.
class AuthorInfo(models.Model):
    photo = models.ImageField(upload_to='author_photo/')
    name = models.CharField('Имя', max_length=50)
    bio = models.TextField('Биография')
    tg = models.CharField('TG', max_length=150)
    vk = models.CharField('VK', max_length=150)
    ig = models.CharField('IG', max_length=150)
    email = models.EmailField('Email', max_length=150)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Информация об авторе"
        verbose_name_plural = "Информация об авторе"

class ArtGroup(models.Model):
    title = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f'{self.title}'

class Collection(models.Model):
    title = models.CharField('Название')

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    def __str__(self):
        return f'{self.title}'

class Artwork(models.Model):
    title = models.CharField('Название', max_length=150)
    group = models.ForeignKey(ArtGroup, on_delete=models.SET_NULL, null=True, related_name='groups', blank=True)
    image = models.ImageField(upload_to='artworks/')
    description = models.TextField('Описание')
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.IntegerField('Год выпуска')
    favorite = models.BooleanField('Избранное', default=False)
    
    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return f'{self.title}'
    

class Appeal(models.Model):
    name = models.CharField('Имя', max_length=150)
    email = models.EmailField('Email', max_length=150)
    theme = models.CharField('Тема', max_length=150)
    message = models.TextField('Сообщение')
    date = models.DateTimeField('Дата и время', auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.theme}'
    
    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
