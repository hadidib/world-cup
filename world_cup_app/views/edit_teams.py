from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Team
from ..serializers import TeamSerializer

class TeamDetailView(generics.RetrieveUpdateAPIView):
    queryset = Team.objects.filter(is_deleted=False)  # Only fetch non-deleted teams
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        team = self.get_object()
        team.is_deleted = True
        team.save()
        return Response({"status": "success", "message": "Team marked as deleted."}, status=status.HTTP_204_NO_CONTENT)
