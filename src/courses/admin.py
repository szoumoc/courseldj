import helpers
from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Course, Lessons



class LessonInline(admin.StackedInline):
    model = Lessons
    readonly_fields = ['public_id',
                       'updated', 
                       'display_image',
                       'display_video'
    ]
    extra = 0

    def display_image(self, obj):
        url = helpers.get_cloudinary_image_object(
            obj,
            field_name='thumbnail',
            width=200
        )
        # cloudinary_id = str(obj.image)
        # cloudinary_html =  CloudinaryImage(cloudinary_id).image(width=200, height=200)
        return format_html(f"<img src='{url}'/>")
    
    def display_video(self, obj):
        video_embed_html = helpers.get_cloudinary_video_object(
            obj,
            field_name='video',
            as_html=True,
            width=550
        )
        # cloudinary_id = str(obj.image)
        # cloudinary_html =  CloudinaryImage(cloudinary_id).image(width=200, height=200)
        return video_embed_html

    display_video.short_description = 'Current video'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['title', 'status', 'access']
    list_filter = ['status', 'access']
    fields = ['public_id','title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['public_id','display_image']

    def display_image(self, obj):
        url = helpers.get_cloudinary_image_object(
            obj,
            field_name='image',
            width=200
        )
        # cloudinary_id = str(obj.image)
        # cloudinary_html =  CloudinaryImage(cloudinary_id).image(width=200, height=200)
        return format_html(f"<img src='{url}'/>")

    display_image.short_description = 'Current Image'


    



