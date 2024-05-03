from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import News

class NewsDeleteView(APIView):
    def delete(self, request, pk, format=None):
        try:
            news = News.objects.get(pk=pk)
            news.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except News.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
