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

class PublishStatus(models.TextChoices):
    PUBLISHED = 'pub', 'Published'
    DRAFT = 'draft', 'Draft'
    COMING_SOON = 'soon', 'Coming Soon'


class AccessRequirement(models.TextChoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'

def handle_upload(instance, filename):
    return f"{filename}"



class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=handle_upload, blank=True, null=True)

    access = models.CharField(
        max_length=10,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices, 
        default=PublishStatus.DRAFT
    )

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

    def __str__(self):
        return self.title


"""
Lessons
    Title
    Description
    Video
    Status: Published, Coming Soon, Draft
"""

