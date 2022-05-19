import json
import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

@api_view(['GET', 'POST'])
def ManageItemsView(request):
    if request.method == 'GET':
        items, count = {}, 0
        for key in redis_instance.keys("*"):
            items[key.decode('utf-8')] = redis_instance.get(key)
            count += 1
        response = {
            'count': count,
            'msg': f"Have found {count} items.",
            'items': items,
        }
        return Response(response, status=200)
    elif request.method == 'POST':
        print(request.body)
        item = json.loads(request.body)
        key = list(item.keys())[0]
        val = item[key]
        redis_instance.set(key, val)
        response = {
            'msg': f"{key} successfully set to {val}."
        }
        return Response(response, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def ManageItemView(request, key):
    if request.method == 'GET':
        if key:
            value = redis_instance.get(key)
            if value:
                response = {
                    'key': key,
                    'value': value,
                    'msg': 'success'
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': key,
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)

    elif request.method == 'PUT':
        if key:
            request_data = json.loads(request.body)
            new_value = request_data['new_value']
            value = redis_instance.get(key)
            if value:
                redis_instance.set(key, new_value)
                response = {
                    'key': key,
                    'value': value,
                    'msg': f"Successfully updated {key}"
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': key,
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)

    elif request.method == 'DELETE':
        if key:
            result = redis_instance.delete(key)
            if result == 1:
                response = {
                    'msg': f"{key} successfully deleted"
                }
                return Response(response, status=404)
            else:
                response = {
                    'key': key,
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)