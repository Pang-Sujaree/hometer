from django.core.management.base import BaseCommand
from dashboard.models import ThingSpeakData
import requests
import json
from celery import Celery

#@Celery.task
class Command(BaseCommand):
    help = 'Fetch data from ThingSpeak and save to PostgreSQL'

    def handle(self, *args, **kwargs):
        # Your ThingSpeak channel URL
        thingspeak_url = "https://api.thingspeak.com/channels/2382430/feeds.json?api_key=LK64S93O4ATUW3EG&results=1"

        # Fetch data from ThingSpeak
        response = requests.get(thingspeak_url)
        data = json.loads(response.text)

        # Extract data and save to PostgreSQL
        for feed in data['feeds']:
            ThingSpeakData.objects.create(
                voltage=feed['field1'],
                current=feed['field2'],
                power=feed['field3'],
                energy=feed['field4'],
                created_at=feed['created_at']
            )

        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved data from ThingSpeak'))
