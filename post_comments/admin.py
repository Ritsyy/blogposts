from django.contrib import admin

from .models import *


class BlogAdmin(admin.ModelAdmin):
    pass


class ParagraphAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(Comment, CommentAdmin)
