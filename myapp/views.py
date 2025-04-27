from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class Example(APIView):
    def get(self, request):
        return Response({'message': 'Hello World'})
    
    def post(self, request):
        name = request.data.get('name')
        message = request.data.get('message')

        if not name or not message:
            return Response({'error': 'name or message are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'result': f"{name}: {message}"
        }, status=status.HTTP_201_CREATED)
