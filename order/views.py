from rest_framework import viewsets
from .serializer import OrderSerializer
from .models import OrderModel



class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

    def delete(self, request, pk):
        order = get_object_or_404(OrderModel, pk=pk)
        order.delete()
        return Response({'message': 'Order deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        order = get_object_or_404(OrderModel, pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

