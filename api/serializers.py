from dataclasses import field, fields
from statistics import mode
from rest_framework import serializers
from base.models import Period

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'