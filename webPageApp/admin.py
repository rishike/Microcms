from django.contrib import admin

# Register your models here.
from django.contrib import admin
from webPageApp.models import WebPage, PageSection, \
            Country, City, Vendor, Device, Lead, WalkIn



admin.site.register(WebPage)
admin.site.register(PageSection)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Vendor)
admin.site.register(Device)
admin.site.register(Lead)
admin.site.register(WalkIn)
