from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Match
from ..serializers import MatchSerializer

class MatchDetailView(generics.RetrieveAPIView):
    queryset = Match.objects.filter(is_deleted=False)
    serializer_class = MatchSerializer

class MatchUpdateView(generics.UpdateAPIView):
    queryset = Match.objects.filter(is_deleted=False)
    serializer_class = MatchSerializer

class MatchDeleteView(generics.UpdateAPIView):
    queryset = Match.objects.filter(is_deleted=False)
    serializer_class = MatchSerializer

    def delete(self, request, *args, **kwargs):
        match = self.get_object()
        match.is_deleted = True
        match.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
