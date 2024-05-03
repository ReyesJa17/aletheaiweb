from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # Optional field
    image = models.ImageField(upload_to='post_images/')  # Ensure you have Pillow installed
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title