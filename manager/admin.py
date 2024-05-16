from django.contrib import admin
from .models import jar, servers, bedrock, modded, vanilla, proxies


class jar_admin(admin.ModelAdmin):
  verbose_name='Jar'
  list_display = ('version', 'project', 'file_size', 'file_hash', 'date_added')
  # search_fields = ('version', 'software')
  list_filter = ('version', 'software', 'project')

class servers_admin(admin.ModelAdmin):
  verbose_name='Server'
  plural_name='Servers'


class modded_admin(admin.ModelAdmin):
  verbose_name='Modded'
  plural_name='Modded'

class bedrock_admin(admin.ModelAdmin):
  verbose_name='Bedrock'
  plural_name='Bedrock'

class vanilla_admin(admin.ModelAdmin):
  verbose_name='vanilla'
  plural_name='vanilla'

class proxies_admin(admin.ModelAdmin):
  verbose_name='Proxy'
  plural_name='proxies'


admin.site.register(jar, jar_admin)

admin.site.register(servers, servers_admin)
admin.site.register(bedrock, bedrock_admin)
admin.site.register(modded, modded_admin)
admin.site.register(vanilla, vanilla_admin)
admin.site.register(proxies, proxies_admin)