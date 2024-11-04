from django.db import models
import uuid

# Create your models here.
class BlogModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_covers/', blank=True, null=True)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "blogs"
        ordering = ['-createdAt']

    def __str__(self):
        return f'{self.title} - Created At: {self.createdAt}'

