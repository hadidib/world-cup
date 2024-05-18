from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Scorer

@api_view(['POST'])
def delete_scorer(request, id):
    try:
        scorer = Scorer.objects.get(id=id)
        scorer.is_deleted = True
        scorer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Scorer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
