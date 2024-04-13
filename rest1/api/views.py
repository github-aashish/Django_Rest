from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.
#Model Object - Single Student Data

def student_detail(request):
    stu = Student.objects.get(id = 1)
    #print(stu)
    serializer = StudentSerializer(stu)
    #print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type="application/json")

def student_detail_by_id(request,pk):
    stu = Student.objects.get(id = pk)
    #print(stu)
    serializer = StudentSerializer(stu)
    #print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type="application/json")

# Query Set All students data
def student_list(request):
    stu = Student.objects.all()
    #print(stu)
    serializer = StudentSerializer(stu, many=True)
    #print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type="application/json")

# we can also use JsonResponse to return response
def easyapi(request,pk):
    stu = Student.objects.get(id = pk)
    #print(stu)
    serializer = StudentSerializer(stu)
    #print(serializer)
    #json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    #return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializer.data)
    #return JsonResponse(serializer.data, safe=False)  use in case og query set 