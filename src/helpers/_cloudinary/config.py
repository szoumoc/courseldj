import cloudinary
from django.conf import settings

# Configuration    
CLOUDINARY_CLOUD_NAME = settings.CLOUDINARY_CLOUD_NAME
CLOUDINARY_API_KEY = settings.CLOUDINARY_API_KEY
CLOUDINARY_API_SECRET = settings.CLOUDINARY_API_SECRET



def cloudinary_init():   
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME,
        api_key = CLOUDINARY_API_KEY,
        api_secret = CLOUDINARY_API_SECRET,
        secure=True
    )