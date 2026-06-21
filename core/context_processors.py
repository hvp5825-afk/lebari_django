from .models import FrontendSection, FeatureItem, CounterItem, ClientLogo, SiteSetting, ButtonSetting

def cms_context(request):
    context = {}

    try:
        context['settings'] = SiteSetting.objects.first()
    except Exception:
        context['settings'] = None

    try:
        context['buttons'] = {b.identifier: b for b in ButtonSetting.objects.all()}
    except Exception:
        context['buttons'] = {}

    try:
        context['sections'] = {s.identifier: s for s in FrontendSection.objects.all()}
    except Exception:
        context['sections'] = {}

    try:
        from .models import SiteLabel
        context['labels'] = {lbl.key: lbl.value for lbl in SiteLabel.objects.all()}
    except Exception:
        context['labels'] = {}



    context['features'] = FeatureItem.objects.all()
    context['counters'] = CounterItem.objects.all()
    context['clients'] = ClientLogo.objects.all()

    try:
        from .models import MenuItem
        menu_items = list(MenuItem.objects.filter(parent__isnull=True).prefetch_related('children').order_by('order'))
        current_path = request.path
        
        # Calculate active state dynamically
        for item in menu_items:
            item.is_active = False
            if item.url and item.url != '#' and item.url in current_path:
                # Basic check, but better to check exact match or exact child match
                # Wait, if item.url == '/', then it's in every path.
                if item.url == '/':
                    if current_path == '/':
                        item.is_active = True
                else:
                    if current_path.startswith(item.url):
                        item.is_active = True
            
            # Check children
            for child in item.children.all():
                child.is_active = False
                if child.url and child.url != '#':
                    if child.url == '/':
                        if current_path == '/':
                            child.is_active = True
                            item.is_active = True
                    elif current_path.startswith(child.url):
                        child.is_active = True
                        item.is_active = True
                        
        context['menu_items'] = menu_items
    except Exception:
        context['menu_items'] = []

    try:
        from .models import FooterColumn
        context['footer_columns'] = FooterColumn.objects.prefetch_related('links').all()
    except Exception:
        context['footer_columns'] = []

    try:
        from .models import SkillBar
        context['skill_bars'] = SkillBar.objects.all()
    except Exception:
        context['skill_bars'] = []

    try:
        from .models import ContactSubject
        context['contact_subjects'] = ContactSubject.objects.all()
    except Exception:
        context['contact_subjects'] = []

    return context

