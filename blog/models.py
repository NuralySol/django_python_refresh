from django.db import models
from django.urls import reverse # This is used to generate URLs by reversing the URL patterns.


# Create your models here. Schema for the database.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=False, blank=False)
    content = models.TextField(max_length=2000, blank=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="images/", blank=True)

    # You can methods to the model to make it more useful.
    def __str__(self):
        return f"{self.title}, {self.slug}"
    # This method is used to generate the URL for the post.
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
