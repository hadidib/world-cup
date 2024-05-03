from rest_framework import generics
from ..models import News
from ..serializers import NewsSerializer
from rest_framework.response import Response

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-date')  # Ordering by 'date' descending
    serializer_class = NewsSerializer

    def list(self, request, *args, **kwargs):
        response = super(NewsListView, self).list(request, *args, **kwargs)
        return Response({'data': response.data}, status=response.status_code)
