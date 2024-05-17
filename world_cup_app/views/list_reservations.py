from rest_framework import generics
from ..models import Reservation
from ..serializers import ReservationlistSerializer

class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationlistSerializer
