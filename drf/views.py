from django.shortcuts import get_object_or_404

from . import models
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import Currency
from .serializers import TodoSerializer, UserSerializer, CurrecySerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from account.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# function base view
# @api_view(['GET', 'POST'])
# def todoserilazers(request: Request):
#     if request.method == 'GET':
#         todos = models.Todo.objects.all().order_by('priority')
#         todo_serializer = TodoSerializer(todos, many=True)
#         return Response(todo_serializer.data, status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#     else:
#         Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, todo_id):
    try:
        todo = models.Todo.objects.get(pk=todo_id)
    except models.Todo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_200_OK)

# end function base view

# end class base view


class TodoManageApiView(APIView):
    def get(self, request: Request):
        todos = models.Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(APIView):
    def get_object(self, todo_id):
        try:
            todo = models.Todo.objects.get(pk=todo_id)
            return todo
        except models.Todo.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, todo_id):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, todo_id):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, todo_id):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


class TodoListMixinsApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class TodoDetailMixinsApiView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)


class TodoGenericsApiView(generics.ListAPIView):
    # class GenericPageinating(PageNumberPagination):
    #     page_size = 3
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    # pagination_class = GenericPageinating
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class TodoDetailGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


class TodoViewSetApiView(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


class UserGenericsApiView(generics.ListAPIView):
    # class UserPageinating(PageNumberPagination):
    #     page_size = 2
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = UserPageinating
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class UserDetailGenericsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrencyListApiView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrecySerializer


class CurrencySymbol(APIView):
    def get(self, request: Request, symbol):
        try:
            symboll = Currency.objects.get(name=symbol)
        except Currency.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        serializer = CurrecySerializer(symboll, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)



def token(request):
