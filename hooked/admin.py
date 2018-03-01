
from django.contrib import admin


class HooksTransactions(admin.ModelAdmin):
    
    date_heirarchy = ('created', )
    list_display = ('signature', 'status', 'app_name')
    readonly_fields = [
        'body', 'meta', 'status', 'modified', 
        'created', 'app_name', 'signature' 
    ]
    
    fieldsets = (
        ('Data', {
            'fields': ('signature', 'body', 'meta', 'status', )
        }),
        ('Logs', {
            'fields': ('app_name', 'modified', 'created', )
        }),
    )
    
    def app_name(self, instance):
        return instance.app.name

    def signature(self, instance):
        return instance.signature


class HooksClientApps(admin.ModelAdmin):
    
    date_heirarchy = ('modified', )
    list_display = ('name', 'modified', )
    
    readonly_fields = ['identifier', 'secret', 'modified', 'created', ]

    fieldsets = (
        ('App info', {
            'fields': ('name', )
        }),
        ('Security', {
            'fields': ('need_authorization', 'identifier', 'secret', )
        }),
        ('Logs', {
            'fields': ('modified', 'created', )
        }),
    )
