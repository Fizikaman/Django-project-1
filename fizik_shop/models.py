from django.db import models
from django.utils import timezone


# Create your models here.

# Создание таблицы в БД
class Category(models.Model):
    # поля в таблице
    title = models.CharField(max_length=255)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):  # магический метод (конвертация в строку) для отображения категории в панели админа
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
