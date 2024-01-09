from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# Create your views here.
from .models import Course


# функция для запроса от клиента и возврата ответа
def index(request):
    courses = Course.objects.all()
    return render(request, 'fizik_shop/courses.html', {'courses': courses}) # использование шаблона HTML для отображения страницы клиенту

# функция для поиска id курса и перехода на страницу курса
def single_course(request, course_id):
    # #Option 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'single_course.html', {'course':course})
    # except Course.DoesNotExist:
    #     raise Http404()

    # Option 2
    course = get_object_or_404(Course, pk=course_id) # функция для обработки ошибки 404
    return render(request, 'fizik_shop/single_course.html', {'course':course})
