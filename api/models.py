from django.db import models
from tastypie.resources import ModelResource
from fizik_shop.models import Category, Course
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization
# Create your models here.

class CategoryResource(ModelResource):
    class Meta: # собс атрибут класса Кат.Ресурс
        queryset = Category.objects.all() # получаем категории из БД
        resource_name = 'categories'
        allowed_methods = ['get'] # разрешенное методы для Категории

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        excludes = ['reviews_qty', 'created_at']
        authentication = CustomAuthentication()
        authorization = Authorization()

    #данные от клиента
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    #данные клиенту
    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle
