from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_mail_author_by_book_register
from .models import Book

@receiver(post_save, sender=Book)
def send_mail_author(sender, instance, created, **kwargs):

    if instance.accepted ==  True:
        subject = 'Activate Your MySite Account'
        message = render_to_string('api/templates/notify_register_book.html', {
            'book': instance,
            'domain': 'localhost:8000',
        })

    send_mail_author_by_book_register.delay(subject, message, settings.EMAIL_HOST_USER, [instance.author.email])