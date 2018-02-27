from rest_framework import serializers

from .models import *


class BlogSerializer(serializers.ModelSerializer):

    paras = serializers.SerializerMethodField()
    paginate_by = 10

    def get_paras(self, obj):
        paragraph = obj.paragraph_set.all()
        paras_serializer = ParagraphSerializer(paragraph, many=True)
        return paras_serializer.data

    class Meta:
        model = Blog
        fields = ('title', 'text', 'paras', 'id')


class ParagraphSerializer(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comment = obj.comment_set.all()
        comment_serializer = CommentSerializer(comment, many=True)
        return comment_serializer.data

    class Meta:
        model = Paragraph
        fields = ('paragraph', 'comments', 'id')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('comment',)
