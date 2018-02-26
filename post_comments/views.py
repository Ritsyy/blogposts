from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class BlogView(APIView):

    serializer_class = BlogSerializer
    allowed_methods = ['GET']

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        response = Response(serializer.data)
        return response

    def get_params(self, obj, blog_id):
        blog = Blog.objects.get(id=blog_id)
        # paragraphs = blog.paragraph_set.all()
        serializer = BlogSerializer(blog, many=True).data
        response = Response(serializer.data)
        return response
