from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

#admin.site.register(background)
admin.site.register(App)
admin.site.register(Title)
admin.site.register(Description)
admin.site.register(Trailer)
admin.site.register(Image)

admin.site.site_header = "Administración de Smart Homy"
admin.site.site_title = "Smart Homy Admin"
#admin.site.index_title = "Smart Homy Admin"
