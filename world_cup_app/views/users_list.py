from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from ..serializers import UserSerializer  # Assume you have a serializer for User model
from rest_framework.permissions import IsAuthenticated

class NonStaffUserListView(ListAPIView):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]