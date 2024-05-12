from rest_framework import serializers
from ..models import Match, Team, Stadium

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'logo']  # Assuming 'image' field holds URL to team's logo

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['id', 'name', 'location', 'seats']  # Assuming these are the fields in your Stadium model

class MatchSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer(read_only=True)
    team2 = TeamSerializer(read_only=True)
    stadium = StadiumSerializer(read_only=True)

    class Meta:
        model = Match
        fields = [
            'id', 'team1', 'team2', 'date', 'stadium', 
            'team1_score', 'team2_score', 
            'price1', 'price2', 'price3', 'type', 'is_played'
        ]

    def validate(self, data):
        """
        Check that team1 and team2 are not the same.
        """
        if 'team1' in data and 'team2' in data and data['team1'] == data['team2']:
            raise serializers.ValidationError("A team cannot play a match against itself.")
        return data
