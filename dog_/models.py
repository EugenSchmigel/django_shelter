from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Poroda')
    description = models.TextField(**NULLABLE, verbose_name='Opisanie')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'poroda'
        verbose_name_plural = 'porody'


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Klichka')
    #category = models.CharField(max_length=100, verbose_name='Poroda')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Poroda')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='Foto')
    birth_day = models.DateTimeField(**NULLABLE, verbose_name='Data Rozhdenie')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Owner')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'sobaka'
        verbose_name_plural = 'sobaki'


class Parent(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name='Klichka')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Poroda')
    birth_day = models.DateTimeField(**NULLABLE, verbose_name='Data Rozhdenie')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'predok'
        verbose_name_plural = 'predki'