from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def api_view(request):
    return HttpResponse("<h1>Hello, World!</h1>")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ExampleView(APIView):
    def get(self, request, format=None):
        data = {"message": "Hello, World!"}
        return Response(data)
