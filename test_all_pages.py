import os
import django
from django.test.client import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_project.settings')
django.setup()

client = Client()

urls_to_test = [
    '/',
    '/about.html',
    '/courses/',
    '/blog/',
    '/contact.html',
    '/faq.html',
    '/teacher.html',
    '/login/',
    '/register/',
]

print("Testing all endpoints...")
all_passed = True
for url in urls_to_test:
    try:
        response = client.get(url)
        if response.status_code == 200:
            print(f"[OK] {url} loaded successfully (200 OK).")
        else:
            print(f"[ERROR] {url} returned status code {response.status_code}.")
            all_passed = False
    except Exception as e:
        print(f"[EXCEPTION] {url} failed with error: {e}")
        all_passed = False

if all_passed:
    print("\nAll tested endpoints are working perfectly and returning 200 OK!")
else:
    print("\nSome endpoints have issues.")
