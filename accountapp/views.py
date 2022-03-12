from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello World! 안녕 홍지현 ?!')
