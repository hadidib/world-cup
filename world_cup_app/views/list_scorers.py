from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Scorer
from ..serializers import ScorerlistSerializer

@api_view(['GET'])
def scorer_list(request):
    scorers = Scorer.objects.filter(is_deleted=False).order_by('-goals')
    serializer = ScorerlistSerializer(scorers, many=True)
    return Response(serializer.data)
