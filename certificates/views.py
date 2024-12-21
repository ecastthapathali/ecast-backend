import secrets
import string
from django.http import HttpResponse, JsonResponse
from PIL import Image, ImageDraw, ImageFont
import io
from textwrap import fill
from .models import ParticipationCertificate
from django.conf import settings
import cloudinary.uploader
import cloudinary.api
from cloudinary.exceptions import Error  

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET
)


event_configurations = {
    'Workshop On django': {
        'name_position': (1000, 710),
        'thanks_message_position': (562, 830),
        'event_name_position': (1051, 830),
        'event_date_position': (1559, 830),
        'held_on_position': (1312, 830),
        'message_positions': {
            'msg1': (1000, 873),
            'msg2': (1010, 913),
            'msg3': (1020, 950),
        },
    },
    'Workshop on AI': {
        'name_position': (1000, 710),  
        'thanks_message_position': (595, 830),
        'event_name_position': (1055, 830),  
        'event_date_position': (1530, 830),  
        'held_on_position': (1300, 830),
        'message_positions': {
            'msg1': (1000, 873),
            'msg2': (1010, 913),
            'msg3': (1020, 950),
        },
    },
}

def generate_random_uid():
    characters = string.ascii_letters + string.digits  
    uid = ''.join(secrets.choice(characters) for _ in range(28)) 
    
    
    formatted_uid = '-'.join([uid[i:i+4] for i in range(0, len(uid), 4)])
    return formatted_uid

def generate_participation_certificate(request):
    
    name = request.GET.get('name')
    event_name = request.GET.get('event_name')

    if not name or not event_name:
        return HttpResponse("Missing required parameters", status=400)

    
    try:
        certificate = ParticipationCertificate.objects.get(name=name, event_name=event_name)
    except ParticipationCertificate.DoesNotExist:
        return HttpResponse("No participation record found for this name and event", status=404)

    custom_id = certificate.custom_id 

    
    try:
        cloudinary.api.resource(f"certificates/{custom_id}")
        certificate_url = f"https://res.cloudinary.com/{settings.CLOUDINARY_CLOUD_NAME}/image/upload/v{certificate.generated_at.year}/{custom_id}.png"
        return JsonResponse({"id": custom_id, "url": certificate_url})

    except Error as e:
        print(f"Error checking resource: {e}")
        pass  

    
    event_config = event_configurations.get(event_name)

    if not event_config:
        return HttpResponse("Event configuration not found", status=404)

    try:
        
        template_path = 'static/certificates/template.png'
        image = Image.open(template_path)
        draw = ImageDraw.Draw(image)

       
        name_font = ImageFont.truetype("static/admin/fonts/Roboto-Bold-webfont.woff", 80)
        event_font = ImageFont.truetype("static/admin/fonts/Roboto-Bold-webfont.woff", 40)
        date_font = ImageFont.truetype("static/admin/fonts/Roboto-Bold-webfont.woff", 40)
        thanks_font = ImageFont.truetype("static/admin/fonts/Roboto-Regular-webfont.woff", 40)

        
        draw.text(event_config['name_position'], name, font=name_font, fill="black", anchor="mm")
        thanks_message = f"for your valuable participation in "
        wrapped_message = fill(thanks_message, width=80)
        bbox = draw.textbbox((0, 0), wrapped_message, font=thanks_font)
        text_width = bbox[2] - bbox[0]
        start_x = event_config['thanks_message_position'][0]
        end_x = start_x + text_width
        draw.text((start_x, event_config['thanks_message_position'][1]), wrapped_message, font=thanks_font, fill="black", anchor="mm")

        
        event_date = certificate.date.strftime('%d %B, %Y')  
        draw.text(event_config['event_name_position'], event_name, font=event_font, fill="black", anchor="mm")
        draw.text(event_config['event_date_position'], event_date, font=date_font, fill="black", anchor="mm")

        
        held_on_message = "held on"
        wrapped_held_on_message = fill(held_on_message, width=80)
        draw.text(event_config['held_on_position'], wrapped_held_on_message, font=thanks_font, fill="black", anchor="mm")

        
        draw.text(event_config['message_positions']['msg1'], "Your presence and contribution made this event a success. We appreciate", font=thanks_font, fill="black", anchor="mm")
        draw.text(event_config['message_positions']['msg2'], "your time and effort in attending, and we hope to see you at", font=thanks_font, fill="black", anchor="mm")
        draw.text(event_config['message_positions']['msg3'], "future events.", font=thanks_font, fill="black", anchor="mm")

    
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        
        response = cloudinary.uploader.upload(buffer, public_id=f"certificates/{custom_id}")
        certificate_url = response["secure_url"]

        
        return JsonResponse({"id": custom_id, "url": certificate_url})

    except Exception as e:
        print(f"Error generating certificate: {e}")
        return HttpResponse("Internal Server Error", status=500)
