from django.contrib import admin

# Register your models here.
admin.site.site_header = 'Sendesta | Admin'
admin.site.index_title = 'Sendesta'
admin.site.site_title = 'Admin'
from .models import Plan ,StripeCustomer

admin.site.register(Plan)
admin.site.register(StripeCustomer)