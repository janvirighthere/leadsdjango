from .models import Lead
from rest_framework import viewsets, permissions
from .serlializers import LeadSerlializer

# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = LeadSerlializer
