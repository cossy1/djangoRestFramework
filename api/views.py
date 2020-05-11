from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions


class StudentApiView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAuthenticated]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# class StudentApiView(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field = 'id'
#     permission_classes = [permissions.IsAuthenticated]
#
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     lookup_field = 'id'
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



#
# class StudentApiView(APIView):
#
#     def get(self, request):
#         a = Student.objects.all()
#         serializer = StudentSerializer(a, many=True)
#         return Response(serializer.data)
#
#     def post(self, requst, *args, **kwargs):
#         parser_class = (FileUploadParser,)
#         if requst.method == 'POST':
#             serializer = StudentSerializer(data=requst.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class StudentDetail(APIView):
#
#     @csrf_exempt
#     def get_object(self, id):
#         try:
#             return Student.objects.get(id=id)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     @csrf_exempt
#     def get(self, request, id):
#         try:
#             a = self.get_object(id)
#             serializer = StudentSerializer(a)
#             return Response(serializer.data)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     @csrf_exempt
#     def put(self, request, id):
#         a = self.get_object(id)
#         serializer = StudentSerializer(a, data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#
#     @csrf_exempt
#     def delete(self, request, id):
#         a = self.get_object(id)
#         a.delete()
#         return Response({'message': 'deleted successfully'})


