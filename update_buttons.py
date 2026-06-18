import os

base_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates"

replacements = [
    ("login.html", "Login</button>", "{{ buttons.login|default:'Login' }}</button>"),
    ("register.html", "Register</button>", "{{ buttons.register|default:'Register' }}</button>"),
    ("contact.html", "Send Message</button>", "{{ buttons.send_message|default:'Send Message' }}</button>"),
    ("blog-detail.html", "<span class=\"txt\">Post comment</span></button>", "<span class=\"txt\">{{ buttons.post_comment|default:'Post comment' }}</span></button>"),
    ("course-detail.html", "Write A Review</button>", "{{ buttons.write_review|default:'Write A Review' }}</button>"),
    ("profile.html", "Update Profile</button>", "{{ buttons.update_profile|default:'Update Profile' }}</button>"),
]

for filename, old_text, new_text in replacements:
    path = os.path.join(base_dir, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content.replace(old_text, new_text)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Not found: {filename}")
