from rest_framework import generics
from ..models import Stadium
from ..serializers import StadiumSerializer

class StadiumCreateView(generics.CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
