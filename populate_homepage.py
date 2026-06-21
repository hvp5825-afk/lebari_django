import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari.settings')
django.setup()

from core.models import HomePageSetting

if not HomePageSetting.objects.exists():
    HomePageSetting.objects.create()
    print("Default HomePageSetting created.")
else:
    print("HomePageSetting already exists.")
