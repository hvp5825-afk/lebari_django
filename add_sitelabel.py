with open('core/models.py', 'a', encoding='utf-8') as f:
    f.write('''

class SiteLabel(models.Model):
    key = models.CharField(max_length=50, unique=True, help_text="Do not change this key once created, as it's used in HTML templates.")
    value = models.CharField(max_length=255, help_text="The actual text that will be displayed on the website.")
    description = models.CharField(max_length=255, blank=True, null=True, help_text="Where is this label used?")
    
    class Meta:
        verbose_name = 'Site Label & Text'
        verbose_name_plural = 'Site Labels & Texts'
        ordering = ['key']
        
    def __str__(self):
        return f"{self.key} : {self.value}"
''')

with open('core/admin.py', 'a', encoding='utf-8') as f:
    f.write('''
from .models import SiteLabel

@admin.register(SiteLabel)
class SiteLabelAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'description')
    search_fields = ('key', 'value', 'description')
''')
