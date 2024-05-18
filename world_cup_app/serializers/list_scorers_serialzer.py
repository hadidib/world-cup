from rest_framework import serializers
from ..models import Scorer

class ScorerlistSerializer(serializers.ModelSerializer):
    team = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = Scorer
        fields = ['id', 'name', 'goals', 'team', 'position', 'matches_played']
