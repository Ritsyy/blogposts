from django.shortcuts import render
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class BlogListView(APIView):

    serializer_class = BlogSerializer
    allowed_methods = ['GET']

    def get(self, request):
        blogs = Blog.objects.all()
        paginator = Paginator(blogs, 5)
        page = request.GET.get('page')
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            blogs = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            blogs = paginator.page(paginator.num_pages)
        serializer = BlogSerializer(blogs, many=True)
        for blog in serializer.data:
            blog.pop('paras')
        response = Response(serializer.data)
        return response


class BlogDetailView(APIView):

    serializer_class = BlogSerializer
    allowed_methods = ['GET']

    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        serializer = BlogSerializer(blog)
        response = Response(serializer.data)
        return response
