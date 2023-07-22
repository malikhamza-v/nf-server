from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from .models import CustomUserModel
from .serializers import CreateUserSerializer, LoginSerializer
from knox import views as knox_views
from rest_framework import status


class CreateUserAPI(CreateAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

class LoginAPI(knox_views.LoginView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(response.data, status=status.HTTP_200_OK)