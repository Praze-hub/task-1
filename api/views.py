from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_info(request):
    data = {
        'email': 'godpraiseokechukwu07@gmail.com',
        'current_datatime': timezone.now().isoformat(),
        'github_url': 'https://github.com/Praze-hub/task-1',
    }
    return Response(data, status=status.HTTP_200_OK)

