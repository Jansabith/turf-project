from twilio.rest import Client
from django.conf import settings

def send_whatsapp(phone_number, message):
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=settings.TWILIO_WHATSAPP_FROM,
            to=f"whatsapp:+91{phone_number}"
        )
    except Exception as e:
        print(f"WhatsApp send failed: {e}")