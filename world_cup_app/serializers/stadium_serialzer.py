from rest_framework import serializers
from ..models import Stadium

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'  # or list specific fields if you want to exclude some
