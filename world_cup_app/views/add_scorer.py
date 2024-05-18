from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Scorer
from ..serializers import ScorerSerializer

@api_view(['POST'])
def scorer_create_api(request):
    if request.method == 'POST':
        serializer = ScorerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
