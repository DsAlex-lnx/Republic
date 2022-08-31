from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .api.serializers import UserSerializer

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'name': user.username,
            'email': user.email,
            'phone': user.locator.phone
        },
        'token': token
    })


@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info': {
                'id':user.id,
                'name': user.username,
                'email': user.email,
                'phone': user.locator.phone
            }
        })

    return Response({'error': 'not authenticated'}, status=400)


@api_view(['POST'])    
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'name': user.username,
            'email': user.email,
            'phone': user.locator.phone
        },
        'token': token
    })