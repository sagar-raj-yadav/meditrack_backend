from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Medicine
from .serializer import MedicineSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .tasks import send_medicine_reminder

# User Registration
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Save User FCM Token
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_fcm_token(request):
    user = request.user
    token = request.data.get("fcm_token")
    
    if token:
        user.medicine_set.update(fcm_token=token)  # Save token for all medicines
        return Response({"message": "FCM token saved"}, status=status.HTTP_200_OK)
    
    return Response({"error": "Token missing"}, status=status.HTTP_400_BAD_REQUEST)

# Medicine CRUD API
class MedicineViewSet(viewsets.ModelViewSet):
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Medicine.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
