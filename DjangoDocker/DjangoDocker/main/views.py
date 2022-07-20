from django.shortcuts import render
from django.conf import settings
import redis


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


def IndexView(request):
    """Index page"""
    if request.method == 'POST':
        key, value = request.POST.get('key'), request.POST.get('value')
        redis_instance.set(key, value)

    context={"redis_keys": redis_instance.keys('*')}

    return render(request, 'main/index.html', context)
