from celery import Celery

from auth.schemas import EmailModel
from mail import mail, create_message
from asgiref.sync import async_to_sync
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

celery_app = Celery()

celery_app.config_from_object("config")


# @c_app.task()
# def send_email(recipients: List[str], subject: str, body: str):
#     message = create_message(recipients=recipients, subject=subject, body=body)
#
#     async_to_sync(mail.send_message)(message)
#     print("Email sent")


@celery_app.task()
def send_email(recipients: EmailModel, subject: str, body: str):
    try:
        # Validate recipients
        if not isinstance(recipients, list) or not all(isinstance(r, str) for r in recipients):
            raise ValueError("Recipients must be a list of strings.")

        # Create the message
        message = create_message(recipients=recipients, subject=subject, body=body)

        # Send the email
        async_to_sync(mail.send_message)(message)
        logger.info("Email sent successfully to %s", recipients)
    except Exception as e:
        logger.error("Failed to send email: %s", str(e))
        raise
