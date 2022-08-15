import json
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status

class TodoListView(APIView):
  def get(self, request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)
  
  def post(self, request, *args, **kwargs):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'ola', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
class TodoEditAndDeleteView(APIView):
  def put(self, request, pk):
    try:
      todo = Todo.objects.get(pk=pk)
      serializer = TodoSerializer(todo, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({"data" :serializer.data, "message": "editado"})
      else:
        return Response({'error': "campo name ta incorreto"}, status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response({'message': "Todo não existe mano"}, status=status.HTTP_400_BAD_REQUEST)
  
  def get(self, reqeust, pk):
    try:
      serializer = TodoSerializer(Todo.objects.get(pk=pk))
      return Response(serializer.data, status=status.HTTP_200_OK)
    except:
      return Response({'message': "Todo não existe mano"}, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    try:
      todo = Todo.objects.get(pk=pk)
      todo.delete()
      return Response({'MEssage': "Deletado com sucesso!"}, status=status.HTTP_200_OK)
    except:
      return Response({'message': "Todo não existe mano"}, status=status.HTTP_400_BAD_REQUEST)
    