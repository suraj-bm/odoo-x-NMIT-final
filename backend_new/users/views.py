from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Register a new user
    """
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Login a user and return JWT tokens
    """
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_200_OK)
    else:
        print("DEBUG ERRORS:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    Logout a user by blacklisting their refresh token
    """
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([AllowAny])
def check_username(request):
    username = request.query_params.get('username', '')
    if not username:
        return Response({'available': False, 'error': 'No username provided'})
    
    exists = User.objects.filter(username=username).exists()
    return Response({'available': not exists})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    Get current user profile
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_by_role(request, role):
    """
    Get users by role
    """
    try:
        users = User.objects.filter(role=role)
        serializer = UserSerializer(users, many=True)
        return Response({
            'role': role,
            'count': users.count(),
            'users': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_by_type(request, user_type):
    """
    Get users by user_type
    """
    try:
        users = User.objects.filter(user_type=user_type)
        serializer = UserSerializer(users, many=True)
        return Response({
            'user_type': user_type,
            'count': users.count(),
            'users': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_roles_info(request):
    """
    Get information about available roles and user types
    """
    return Response({
        'roles': [{'value': choice[0], 'label': choice[1]} for choice in User.ROLE_CHOICES],
        'user_types': [{'value': choice[0], 'label': choice[1]} for choice in User.USER_TYPE_CHOICES],
        'current_user': {
            'username': request.user.username,
            'role': request.user.role,
            'user_type': request.user.user_type,
            'is_admin': request.user.is_admin,
            'is_buyer': request.user.is_buyer,
            'is_seller': request.user.is_seller,
            'is_accountant': request.user.is_accountant,
        }
    }, status=status.HTTP_200_OK)