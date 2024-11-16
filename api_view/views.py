from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person

@api_view(['GET'])
def routes(request):
    routes = [
        'GET api/routes',
        'GET api/person',
    ]
    return Response(routes)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data    
        obj = Person.objects.get(id=data.get('id'))
        serializer = PersonSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data    
        obj = Person.objects.get(id=data.get('id'))
        serializer = PersonSerializer(obj, data=data,  partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
    else:
        data = request.data  
        obj = Person.objects.get(id=data.get('id'))
        obj.delete()
        return Response({
            'message' : 'Person deleted'
        })