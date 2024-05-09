from rest_framework import generics
from ..models import Match
from ..serializers import MatchSerializer

class MatchListView(generics.ListAPIView):
    queryset = Match.objects.all().select_related('team1', 'team2', 'stadium')
    serializer_class = MatchSerializer
