from rest_framework import generics
from ..models import Stadium
from ..serializers import StadiumSerializer

class StadiumListView(generics.ListAPIView):
    queryset = Stadium.objects.filter(is_deleted=False)
    serializer_class = StadiumSerializer
