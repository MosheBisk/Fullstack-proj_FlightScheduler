from django.contrib import admin
from .models import Schedule 

def oneway_trip(modeladmin, request, querset):
    querset.update(trip_type="Uno way")

class AdminSchedule(admin.ModelAdmin):
    model = Schedule
    list_display = (Schedule, 'id', 'airline', 'flight_no', 'trip_type')
    actions = [oneway_trip]

admin.site.register(Schedule, AdminSchedule)