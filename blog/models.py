from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):

    """When the Post class is queried using the Post.objects interface, only the published objects will be returned."""
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    DRAFT = 'draft'
    PUBLISHED = 'published'

    OPTIONS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )

    # Delete a category is not allowed (hence, PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True) # subtitle
    content = models.TextField()

    # slug allows to use the name as url parameter
    slug = models.SlugField(max_length=250, unique_for_date='published') 
    published = models.DateTimeField(default=timezone.now)

    # CASCADE: If deleted an user, it will delete all posts associated with
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    # Choose post to be in draft or published mode
    status = models.CharField(max_length=10, choices=OPTIONS, default=DRAFT)

    objects = models.Manager()  # All the posts 
    postobjects = PostObjects() # Only the published posts

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title