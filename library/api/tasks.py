from celery import task
from django.core.mail import send_mail

@task(name="send_mail_author_by_book_register")
def send_mail_author_by_book_register(subject, message, sender, receivers):
    send_mail(subject, message, sender, receivers)
