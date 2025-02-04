from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializer

@api_view(['GET'])
def get_info(request):
    data = {
        'email': 'godpraiseokechukwu07@gmail.com',
        'current_datetime': timezone.now().isoformat(),
        'github_url': 'https://github.com/Praze-hub/task-1',
    }
    serializer = EmailSerializer(data=data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

