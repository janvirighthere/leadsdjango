from rest_framework import serializers
from .models import Lead

# Lead Serializer


class LeadSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
