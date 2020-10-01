from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from profile_api.models import UserProfile
from profile_api.serializers import (UserRegisterSerializer,UserLoginSerializer,UserDetailUpdateSerializer,)
from rest_framework import status

class UserRegisterAPI(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'status code' : status_code,
            'message': 'User Register Success',
            }
        return Response(response, status=status_code) 

class UserLoginAPI(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        status_code = status.HTTP_200_OK
        response = {
            'status code' : status_code,
            'message': 'User Login Success',
            'token': AuthToken.objects.create(user)[1]
            }
        return Response(response, status=status_code) 

class UserUpdateAPI(generics.UpdateAPIView):
    serializer_class = UserDetailUpdateSerializer
    permission_classes=(permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user 

    def put(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)
        status_code = status.HTTP_200_OK
        response = {
            'status code' : status_code,
            'message': 'User Update Success',
             }
        return Response(response, status=status_code)

class UserDetailAPI(generics.RetrieveAPIView):
    serializer_class = UserDetailUpdateSerializer
    permission_classes=(permissions.IsAuthenticated,)
    
    def get_object(self):
        return self.request.user  
