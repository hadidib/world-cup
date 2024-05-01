from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from ..serializers import UserSerializer  # Make sure this is correctly imported
from rest_framework.permissions import IsAuthenticated

class StaffUserListView(ListAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]