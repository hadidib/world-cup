from rest_framework import generics
from ..models import Team
from ..serializers import TeamSerializer

class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()  # Fetches all team instances
    serializer_class = TeamSerializer  # Uses your existing serializer to handle data
