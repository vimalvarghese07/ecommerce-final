from rest_framework import viewsets
from .serializer import UserSerializer,UserDetailsSerializer
from django.contrib.auth.models import User
from .models import UserDetailsModel
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    
class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserDetailsModel.objects.all()
    serializer_class = UserDetailsSerializer
    
    def put(self, request, pk):
        user = get_object_or_404(UserDetailsModel, pk=pk)
        serializer = UserDetailsSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = get_object_or_404(UserDetailsModel, pk=pk)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

