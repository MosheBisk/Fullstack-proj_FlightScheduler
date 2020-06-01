from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

# router = DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path('', include(router.urls))
    url(r'^$', views.flight_list),
    url(r'^(?P<prk>[0-9]+)$', views.flight_detail)
]