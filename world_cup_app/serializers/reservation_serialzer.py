# serializers.py

from rest_framework import serializers
from ..models import Reservation, Match, Team

from rest_framework import serializers
from ..models import Reservation, Match

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

class ReservationSerializer(serializers.ModelSerializer):
    match = MatchSerializer()

    class Meta:
        model = Reservation
        fields = ['user', 'match', 'seat_number', 'price', 'date']

class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['user', 'match', 'seat_number', 'price']

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)
