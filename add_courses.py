import os
import django
from django.core.files import File
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_project.settings')
django.setup()

from courses.models import Course, CourseCategory, Teacher

def resize_and_crop(img_path, dest_path, target_size=(370, 240)):
    with Image.open(img_path) as img:
        img = img.convert("RGBA")
        img_aspect = img.width / img.height
        target_aspect = target_size[0] / target_size[1]
        
        if img_aspect > target_aspect:
            new_width = int(target_aspect * img.height)
            offset = (img.width - new_width) / 2
            crop_box = (offset, 0, img.width - offset, img.height)
        else:
            new_height = int(img.width / target_aspect)
            offset = (img.height - new_height) / 2
            crop_box = (0, offset, img.width, img.height - offset)
            
        img = img.crop(crop_box)
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        img = img.convert("RGB")
        img.save(dest_path, "JPEG", quality=95)

def run():
    # Setup Category and Teacher
    cat, _ = CourseCategory.objects.get_or_create(name='Technology', defaults={'slug': 'technology'})
    teacher, _ = Teacher.objects.get_or_create(name='John Doe', defaults={'designation': 'Senior Instructor'})
    
    # Clear existing courses
    Course.objects.all().delete()
    
    courses_data = [
        {
            'title': 'Advanced Data Science Bootcamp',
            'slug': 'advanced-data-science',
            'desc': 'Master data science, machine learning and deep learning with Python.',
            'price': 199.99,
            'orig_price': 299.99,
            'duration': '40.5 hours',
            'level': 'Advanced',
            'img_src': 'learning_laptop_closeup_1781517364967.png'
        },
        {
            'title': 'Full Stack Web Development',
            'slug': 'full-stack-web-dev',
            'desc': 'Learn to build complete web applications from scratch.',
            'price': 149.99,
            'orig_price': 199.99,
            'duration': '55.0 hours',
            'level': 'Beginner to Advanced',
            'img_src': 'hero_student_learning_1781517350974.png'
        },
        {
            'title': 'Digital Marketing Masterclass',
            'slug': 'digital-marketing',
            'desc': 'Grow your business with social media, SEO, and content marketing.',
            'price': 89.99,
            'orig_price': 129.99,
            'duration': '22.5 hours',
            'level': 'All Levels',
            'img_src': 'career_change_1781519768361.png'
        },
        {
            'title': 'UI/UX Design Fundamentals',
            'slug': 'ui-ux-design',
            'desc': 'Create beautiful user interfaces and amazing user experiences.',
            'price': 120.00,
            'orig_price': 150.00,
            'duration': '15.0 hours',
            'level': 'Beginner',
            'img_src': 'feature_main_1781519382215.png'
        },
        {
            'title': 'Machine Learning A-Z',
            'slug': 'machine-learning',
            'desc': 'A comprehensive guide to machine learning concepts and algorithms.',
            'price': 199.99,
            'orig_price': 249.99,
            'duration': '44.0 hours',
            'level': 'Intermediate',
            'img_src': 'feature_main_dark_1781519640150.png'
        },
        {
            'title': 'Photography & Videography',
            'slug': 'photography-videography',
            'desc': 'Learn how to capture stunning photos and cinematic videos.',
            'price': 75.00,
            'orig_price': 99.00,
            'duration': '18.5 hours',
            'level': 'All Levels',
            'img_src': 'special_classroom_1781519954060.png'
        }
    ]
    
    base_dir = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf"
    media_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\media\courses"
    os.makedirs(media_dir, exist_ok=True)
    
    for idx, data in enumerate(courses_data):
        src_path = os.path.join(base_dir, data['img_src'])
        dest_filename = f"course_img_{idx}.jpg"
        dest_path = os.path.join(media_dir, dest_filename)
        
        if os.path.exists(src_path):
            resize_and_crop(src_path, dest_path)
            
            c = Course(
                title=data['title'],
                slug=data['slug'],
                category=cat,
                teacher=teacher,
                description=data['desc'],
                price=data['price'],
                original_price=data['orig_price'],
                duration=data['duration'],
                level=data['level'],
                rating=4.9,
                reviews_count=120 + idx*5
            )
            # Assign the image
            with open(dest_path, 'rb') as f:
                c.image.save(dest_filename, File(f), save=False)
            c.save()
            print(f"Added course: {c.title}")
        else:
            print(f"Missing image for {data['title']}: {src_path}")

if __name__ == '__main__':
    run()
