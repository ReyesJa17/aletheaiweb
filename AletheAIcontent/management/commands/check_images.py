from django.core.management.base import BaseCommand
from AletheAIcontent.models import Image

class Command(BaseCommand):
    help = 'Checks the image records in the database'

    def handle(self, *args, **options):
        images = Image.objects.all()
        for image in images:
            print(f"Image ID: {image.id}")
            print(f"Image File Path: {image.image.url}")
            print("---")