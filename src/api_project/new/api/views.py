from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from new.models import GetInfo
from new.api.serializers import InfoSerializer


@api_view(['GET'])
def api_detail_view(request):

    try:
        queryset = GetInfo.objects.all()
    except GetInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOuND)

    if request.method == "GET":
        serializer = InfoSerializer(queryset, many=True)
        return Response(serializer.data)

