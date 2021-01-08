from django.contrib import admin

from kitchen.models import Category1,Kitchen_base
from kitchen.models import popular1,popular2,popular3

admin.site.register(popular1,)
admin.site.register(popular2)
admin.site.register(popular3)
admin.site.register(Category1)
admin.site.register(Kitchen_base)