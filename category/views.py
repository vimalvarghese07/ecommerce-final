from rest_framework import viewsets
from .serializer import CategorySerializer
from .models import CategoryModel

class GetCategory(viewsets.ModelViewSet):
	queryset = CategoryModel.objects.all()

	serializer_class = CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request, pk):
        category = get_object_or_404(CategoryModel, pk=pk)
        category.delete()
        return Response({'message': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        category = get_object_or_404(CategoryModel, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

