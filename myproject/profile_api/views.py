from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from profile_api.models import UserProfile,UserProject
from profile_api.serializers import (UserRegisterSerializer,UserLoginSerializer,UserDetailUpdateSerializer,ProjectSerializer,)
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

        
'''
---------------------------------------------------------------ProjectAPI----------------------------------------------------------------------------
'''     
   
class ProjectListsAPI(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes=(permissions.IsAuthenticated,)
    
    def get_queryset(self):
       return UserProject.objects.filter(user=self.request.user)
    
class ProjectCreateAPI(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = UserProject.objects.all().order_by('end_date',)
    permission_classes=(permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
            
    def post(self, request, *args, **kwargs):
        status_code = status.HTTP_201_CREATED
        response = {
            'status code' : status_code,
            'message': 'Project Added Success',
             }
        return Response(response, status=status_code)
       

class ProjectUpdateAPI(generics.UpdateAPIView):
    serializer_class = ProjectSerializer
    permission_classes=(permissions.IsAuthenticated,)
        
    def get_queryset(self):
        return UserProject.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user) 
        
    def put(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)
        status_code = status.HTTP_200_OK
        response = {
            'status code' : status_code,
            'message': 'Project Update Success',
             }
        return Response(response, status=status_code)

class ProjectDetailsAPI(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    permission_classes=(permissions.IsAuthenticated,) 
    
    def get_queryset(self):
        return UserProject.objects.filter(user=self.request.user)       