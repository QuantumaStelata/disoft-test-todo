from django.core.mail import EmailMessage

from celery import shared_task


@shared_task
def send_email_to_users(emails):
    return EmailMessage(
        'Task created',
        'You\'ve been added to a task',
        'disoft.test.todo@gmail.com',
        emails,
    ).send()
    
