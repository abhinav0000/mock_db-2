from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import io
from .serializers import studentserializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
# Create your views here.
#deserialization
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        serializer = studentserializer(data= python_data)
        if serializer.is_valid():
            serializer.save()
            res= {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type= 'application/json')