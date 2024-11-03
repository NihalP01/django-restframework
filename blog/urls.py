from .views import Blogs, BlogDetails
from django.urls import path

urlpatterns = [
    path('', Blogs.as_view(), name="all_blogs"),
    path('<str:pk>', BlogDetails.as_view(), name="blog_details")
]
