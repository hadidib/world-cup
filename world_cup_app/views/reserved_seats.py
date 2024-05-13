# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Reservation
from ..serializers import ReservationSerializer

class ReservedSeatsView(APIView):
    def get(self, request, match_id):
        # Assuming the match ID is passed directly in the URL
        reservations = Reservation.objects.filter(match_id=match_id)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
