from __future__ import unicode_literals

from django.apps import AppConfig


class PostCommentsConfig(AppConfig):
    name = 'post_comments'

    def ready(self):
        from .signals import *
