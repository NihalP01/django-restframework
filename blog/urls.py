from .views import Blogs
from django.urls import path

urlpatterns = [
    path('', Blogs.as_view(), name="all_blogs")
]
