from celery import shared_task
from pyfcm import FCMNotification
from django.conf import settings
from .models import Medicine
from django.utils.timezone import localtime, now

push_service = FCMNotification(api_key=settings.FCM_SERVER_KEY)

@shared_task
def send_medicine_reminder():
    current_time = localtime(now()).time()
    medicines = Medicine.objects.filter(time=current_time)

    for medicine in medicines:
        if medicine.fcm_token:  # Check if user has registered their FCM token
            push_service.notify_single_device(
                registration_id=medicine.fcm_token,
                message_title="Medicine Reminder",
                message_body=f"It's time to take your {medicine.name} ({medicine.dosage})"
            )
    return "Push notifications sent"
