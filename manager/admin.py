from django.contrib import admin
from .models import jar, servers, bedrock, modded, vanilla, proxies


class jar_admin(admin.ModelAdmin):
  verbose_name='Jar'
  list_display = ('version', 'software', 'file_size', 'date_added')
  # search_fields = ('version', 'software')
  list_filter = ('version', 'software')



admin.site.register(jar, jar_admin)

admin.site.register(servers)
admin.site.register(bedrock)
admin.site.register(modded)
admin.site.register(vanilla)
admin.site.register(proxies)