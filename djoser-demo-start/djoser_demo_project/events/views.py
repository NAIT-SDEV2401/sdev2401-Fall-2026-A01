from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsOrganizer
from .models import Event, Talk
from .serializers import EventSerializer, TalkSerializer

# TODO Part 2: Create EventAPIView extending APIView
#   - get(self, request, pk=None): return single event by pk, or all events
#   - post(self, request): create a new event (organizer only)
#   - get_permissions(self): return [IsOrganizer()] for POST, [IsAuthenticated()] otherwise

# TODO Part 3: Create TalkViewSet extending viewsets.ModelViewSet
#   - queryset: all Talk objects
#   - serializer_class: TalkSerializer
#   - permission_classes: (IsAuthenticated,)
