import cloudinary
from decouple import config

# Configuration    
CLOUDINARY_CLOUD_NAME = config("CLOUDINARY_CLOUD_NAME", default="")
CLOUDINARY_API_KEY = config("CLOUDINARY_API_KEY", default="549549187356465")
CLOUDINARY_API_SECRET = config("CLOUDINARY_API_SECRET")

def cloudinary_init():   
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME,
        api_key = CLOUDINARY_API_KEY,
        api_secret = CLOUDINARY_API_SECRET,
        secure=True
    )