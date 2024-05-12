# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Reservation
from ..serializers import ReservationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class ReservationCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Add user from request to data before passing it to serializer
        request.data.update({'user': request.user.id})
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
