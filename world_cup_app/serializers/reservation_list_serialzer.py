from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import Reservation, Match, Team

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'logo']

class MatchSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()

    class Meta:
        model = Match
        fields = ['team1', 'team2', 'date']

class ReservationlistSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    match = MatchSerializer()

    class Meta:
        model = Reservation
        fields = ['user', 'match', 'seat_number', 'price', 'date']
