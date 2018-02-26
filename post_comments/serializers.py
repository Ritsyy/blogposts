from rest_framework import serializers

from .models import *


class BlogSerializer(serializers.ModelSerializer):

    paras = serializers.SerializerMethodField()

    def get_paras(self, obj):
        paragraph = obj.paragraph_set.all()
        paras_serializer = ParagraphSerializer(paragraph, many=True)
        return paras_serializer.data

    class Meta:
        model = Blog
        fields = ('title', 'text', 'paras')


class ParagraphSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paragraph
        fields = ('paragraph')


class CommentSerializer(serializers.ModelSerializer):

    paragraph = serializers.RelatedField(source='paragraph', read_only=True)

    class Meta:
        model = Comment
        fields = ('comment', 'paragraph')
