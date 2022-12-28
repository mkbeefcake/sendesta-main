from django.contrib import admin
from .models import (CompanyInformation
,YourBusinessRecommendation
,YourCurrentTradelines
,SendestaScore
,BusinessReports
,UpdateYourCompanyInformation
,Dispute)
# Register your models here.

admin.site.register(CompanyInformation)
admin.site.register(YourBusinessRecommendation)
admin.site.register(YourCurrentTradelines)
admin.site.register(SendestaScore)
admin.site.register(BusinessReports)
admin.site.register(UpdateYourCompanyInformation)
admin.site.register(Dispute)