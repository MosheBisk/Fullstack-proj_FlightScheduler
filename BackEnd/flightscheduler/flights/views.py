from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Schedule
from .serializers import UserSerializer, SchedulerSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("<H1>Hello flight Scheduler!<H1>")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# APIs
#  /flights/

@csrf_exempt
def flight_list(request):
    # Get all
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        schedules_serializer = SchedulerSerializer(schedules, many=True)
        return JsonResponse(schedules_serializer.data, safe=False)

    # Add one
    if request.method == 'POST':
        schedule_data = JSONParser().parse(request)
        schedule_serializer = SchedulerSerializer(data=schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete all
    if request.method == 'DELETE':
        Schedule.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def flight_detail(request, prk):
    try:
        schedule = Schedule.objects.get(pk=prk)
    except Schedule.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NO_FOUND)

    # Retrive one record
    if request.method == 'GET':
        schedule_serializer = SchedulerSerializer(schedule)
        return JsonResponse(schedule_serializer.data)

    # Update one record
    if request.method == 'PUT':
        schedule_data = JSONParser().parse(request)
        schedule_serializer = SchedulerSerializer(schedule, data=schedule_data)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse(schedule_serializer.data)
        return JsonResponse(schedule_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete one record
    if request.method == 'DELETE':
        schedule.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)