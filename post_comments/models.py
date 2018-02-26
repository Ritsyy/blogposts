from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
    title = models.TextField(max_length=200)
    text = models.TextField(null=True)

    def __str__(self):
        return self.title


class Paragraph(models.Model):
    paragraph = models.TextField()
    blog = models.ForeignKey(Blog)

    def __str__(self):
        return self.paragraph


class Comment(models.Model):
    comment = models.TextField()
    paragraph = models.ForeignKey(Paragraph)

    def __str__(self):
        return self.comment
