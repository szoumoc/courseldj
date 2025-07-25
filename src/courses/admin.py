
from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'access']
    list_filter = ['status', 'access']
    fields = ['title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['display_image']

    def display_image(self, obj):
        url = obj.image_admin
        # cloudinary_id = str(obj.image)
        # cloudinary_html =  CloudinaryImage(cloudinary_id).image(width=200, height=200)
        return format_html(f"<img src='{url}'/>")

    display_image.short_description = 'Current Image'




