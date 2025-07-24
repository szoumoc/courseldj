from django.db import models

# Create your models here.
"""Title
Description
Thumbnail/Image
Access:
    Anyone
    Email required
    Purchase required
    User required (n/a)
Status:
    Published
    Coming Soon
    Draft
"""
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='course_thumbnails/')
    access = models.CharField(max_length=50, choices=[
        ('anyone', 'Anyone'),
        ('email_required', 'Email Re quired'),
        ('purchase_required', 'Purchase Required'),
        ('user_required', 'User Required')
    ])
    status = models.CharField(max_length=50, choices=[
        ('published', 'Published'),
        ('coming_soon', 'Coming Soon'),
        ('draft', 'Draft')
    ])

    def __str__(self):
        return self.title


"""
Lessons
    Title
    Description
    Video
    Status: Published, Coming Soon, Draft
"""

