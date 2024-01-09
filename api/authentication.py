# модуль для аутентификации пользователя на удаление и размещения курсов

from tastypie.authentication import ApiKeyAuthentication


class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return super().is_authenticated(request, **kwargs) # временно создается экземпляр родительского класса за счет метода super().

