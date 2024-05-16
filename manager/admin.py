from django.contrib import admin
from .models import jar, servers, bedrock, modded, vanilla, proxies


class jar_admin(admin.ModelAdmin):
  verbose_name='Jar'
  list_display = ('version', 'software', 'file_size', 'file_hash', 'date_added')
  # search_fields = ('version', 'software')
  list_filter = ('version', 'software')

class servers_admin(admin.ModelAdmin):
  verbose_name='Server'
  plural_name='Servers'



admin.site.register(jar, jar_admin)

admin.site.register(servers, servers_admin)
admin.site.register(bedrock)
admin.site.register(modded)
admin.site.register(vanilla)
admin.site.register(proxies)