from rest_framework import generics
from ..models import Team
from ..serializers import TeamSerializer

class TeamListView(generics.ListAPIView):
    queryset = Team.objects.filter(is_deleted=False)  # Only include teams that are not marked as deleted
    serializer_class = TeamSerializer

