from rest_framework import serializers
from ..models import Scorer

class ScorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scorer
        fields = ['name', 'goals', 'team', 'position', 'matches_played']
