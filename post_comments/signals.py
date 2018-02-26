from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *


@receiver(post_save, sender=Blog, dispatch_uid='convert_paragraphs')
def convert_paragraphs(sender, instance, created, **kwargs):
    if created:
        data = instance.text.split('\r\n\r\n')
        for paragraph in data:
            Paragraph.objects.create(paragraph=paragraph, blog=instance)
