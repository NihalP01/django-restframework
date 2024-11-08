from rest_framework.response import Response
from rest_framework import status, generics
from .models import BlogModel
from .serializers import BlogSerializer
from .permissions import IsAdminOrReadOnly
from datetime import datetime

class Blogs(generics.GenericAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

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
        

class BlogDetails(generics.GenericAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_blog(self, pk):
        try:
            return BlogModel.objects.get(pk=pk)
        except BlogModel.DoesNotExist:
            return None
    
    def get(self, request, pk):
        blog = self.get_blog(pk=pk)
        if blog is None:
            return Response({"status": "fail", "message": f'Blog with id {pk} is not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(blog)
        return Response({"status": "Success", "data": {"blog": serializer.data}})
    
    def patch(self, request, pk):
        blog = self.get_blog(pk)
        if blog is None:
            return Response({"status": "fail", "message": f'Blog with id {pk} is not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"blog": serializer.data}})
        return Response({"status": "Fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_blog(pk)
        if blog is None:
            return Response({"status": "fail", "message": f"Unable to delete blog with id: {pk}"}, status=status.HTTP_404_NOT_FOUND)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
