from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class SchedulerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = (  'id',
                    'airline',
                    'flight_no',
                    'trip_type',
                    'departure_airport',
                    'arrival_airport',
                    'departure_date',
                    'return_date'
        )