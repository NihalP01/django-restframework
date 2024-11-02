from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import BlogModel


# Create your views here.
class Blogs(generics.GenericAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()

    def get(self, request):
        blogs = BlogModel.objects.all()
        total_blogs = blogs.count()
        serializer = self.serializer_class(blogs, many=True)
        return Response({
            "total_blogs": total_blogs,
            "blogs": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)