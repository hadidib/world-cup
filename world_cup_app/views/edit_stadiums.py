from rest_framework import generics, status
from rest_framework.response import Response
from ..models import Stadium
from ..serializers import StadiumSerializer

class StadiumDetailView(generics.RetrieveUpdateAPIView):
    queryset = Stadium.objects.filter(is_deleted=False)
    serializer_class = StadiumSerializer

    def delete(self, request, *args, **kwargs):
        stadium = self.get_object()
        stadium.is_deleted = True
        stadium.save()
        return Response({"status": "success", "message": "Stadium marked as deleted."}, status=status.HTTP_204_NO_CONTENT)
