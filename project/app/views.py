from __future__ import unicode_literals

from django.template.response import TemplateResponse

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from app.serializers import *
from app.models import Trip


def index_view(request):
    context = {}
    return TemplateResponse(request, 'index.html', context)


class TripViewSet(MongoModelViewSet):

    lookup_field = '_id'
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.all()
