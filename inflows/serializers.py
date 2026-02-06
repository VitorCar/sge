from rest_framework import serializers
from .models import Inflow


class InflowSerializers(serializers.ModelSerializer):

    class Meta:
        model = Inflow
        fields = '__all__'
