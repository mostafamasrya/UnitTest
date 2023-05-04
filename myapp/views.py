from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from myapp.models import Book
from myapp.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def GetBook(request):
    queryset = Book.objects.all()
    if(queryset):
        mydata = BookSerializer(queryset, many=True)
        return Response(mydata.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)