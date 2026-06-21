with open('core/models.py', 'a', encoding='utf-8') as f:
    f.write('''

class MenuLink(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=255, default='#', help_text="Can be a relative path (e.g. '/about/'), absolute URL, or '#' if it's just a dropdown parent.")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Navigation Menu Link'
        verbose_name_plural = 'Navigation Menu Links'
        
    def __str__(self):
        if self.parent:
            return f"{self.parent.title} > {self.title}"
        return self.title

class FooterColumn(models.Model):
    title = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Footer Column'
        verbose_name_plural = 'Footer Columns'
        
    def __str__(self):
        return self.title

class FooterLink(models.Model):
    column = models.ForeignKey(FooterColumn, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=255, default='#')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Footer Link'
        verbose_name_plural = 'Footer Links'
        
    def __str__(self):
        return f"{self.column.title} -> {self.title}"
''')
