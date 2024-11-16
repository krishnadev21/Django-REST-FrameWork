from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer,  ColorSerializer
from .models import Person, Color
from rest_framework.decorators import action

class ColorViewSet(viewsets.ModelViewSet):
    # Control methods
    # http_method_names = ['get', 'post']
    serializer_class = ColorSerializer
    queryset = Color.objects.all()

class PersonViewSet(viewsets.ModelViewSet):
    # Control methods
    # http_method_names = ['get', 'post']
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith = search)

        serializer = PersonSerializer(queryset, many=True)
        return Response({
            'StatusCode' : 200,
            'data'  : serializer.data
        })
    
    @action(detail=True, methods=['GET'])
    def send_mail_to_user(self, request, pk):
        persons = Person.objects.get(pk=pk)
        serializer = PersonSerializer(persons, many=False)
        return Response({
            'Status' : True,
            'Message' : 'Email sent succesfully.',
            'Persons' : serializer.data
        }, status.HTTP_200_OK)
     
    # Example for detail=False
    # @action(detail=False, methods=['POST'])
    # def send_mail_to_user(self, request):
    #     return Response({
    #         'Status' : True,
    #         'Message' : 'Email sent succesfully.'
    #     }, status.HTTP_200_OK)