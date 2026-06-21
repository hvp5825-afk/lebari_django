import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lebari_project.settings")
django.setup()

from core.models import SkillBar

def run():
    SkillBar.objects.all().delete()

    SkillBar.objects.create(title="Joyful", percentage=90, order=10)
    SkillBar.objects.create(title="Case Study success", percentage=95, order=20)
    SkillBar.objects.create(title="Engaging", percentage=75, order=30)

    print("Skill bars populated!")

if __name__ == '__main__':
    run()
