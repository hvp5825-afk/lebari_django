from .models import FrontendSection, FeatureItem, CounterItem, ClientLogo, SiteSetting, ButtonSetting

def cms_context(request):
    sections = {s.identifier: s for s in FrontendSection.objects.all()}
    features = FeatureItem.objects.all()
    counters = CounterItem.objects.all()
    clients = ClientLogo.objects.all()
    site_setting = SiteSetting.objects.first()
    
    button_settings_qs = ButtonSetting.objects.all()
    buttons = {b.identifier: b.text for b in button_settings_qs}
    
    return {
        'sections': sections,
        'features': features,
        'counters': counters,
        'clients': clients,
        'site_setting': site_setting,
        'buttons': buttons,
    }
