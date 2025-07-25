import helpers
from cloudinary.models import CloudinaryField
from django.db import models



helpers.cloudinary_init()
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
    # thumbnail = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)

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
    

    @property
    def image_admin(self):
        if not self.image:
            return ""
        image_options = {
            'width': 200,
        }

        url = self.image.build_url(**image_options)
        return url
    

    def get_image_thumbnail(self, as_html=False, width=500):
        if not self.image:
            return ""
        image_options = {
            'width': width,
        }
        if as_html:
            return self.image.image(**image_options)
        url = self.image.build_url(**image_options)
        return url
    def get_image_detail(self, as_html=False, width=750):
        if not self.image:
            return ""
        image_options = {
            'width': width,
        }
        if as_html:
            return self.image.image(**image_options)
        url = self.image.build_url(**image_options)
        return url

"""
Lessons
    Title
    Description
    Video
    Status: Published, Coming Soon, Draft
"""

