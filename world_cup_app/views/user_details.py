from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch user from the token
        user = request.user
        return Response({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_staff': user.is_staff
        })