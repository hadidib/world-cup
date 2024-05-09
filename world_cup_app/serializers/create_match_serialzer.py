from rest_framework import serializers
from ..models import Match, Team, Stadium

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'team1', 'team2', 'date', 'stadium', 'team1_score', 'team2_score', 'price1', 'price2', 'price3', 'type']

    def validate(self, data):
        """
        Check that team1 and team2 are not the same.
        """
        if data['team1'] == data['team2']:
            raise serializers.ValidationError("A team cannot play a match against itself.")
        return data
