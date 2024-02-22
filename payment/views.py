from rest_framework import viewsets
from .serializer import PaymentSerializer
from .models import PaymentModel


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer

    def delete(self, request, pk):
        payment = get_object_or_404(CategoryModel, pk=pk)
        payment.delete()
        return Response({'message': 'Payment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        payment = get_object_or_404(PaymentModel, pk=pk)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

