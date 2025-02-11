from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet, register, save_fcm_token

router = DefaultRouter()
router.register(r"medicines", MedicineViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/register/", register),
    path("api/save-fcm-token/", save_fcm_token),  # Save FCM token from the React Native app
]
