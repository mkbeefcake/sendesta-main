from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("inbox", views.Inbox, name="inbox"),
    path("profile", views.Profile, name="profile"),
    path("cancel-membership", views.CancelMembership, name="cancel-membership"),
    path("upgrade-membership", views.UpgradeMembership, name="upgrade-membership"),
    path("your-business-report", views.YourBusinessReport, name="your-business-report"),
    path(
        "your-company-information",
        views.YourCompanyInformation,
        name="your-company-information",
    ),
    path(
        "your-business-tradelines",
        views.YourBusinessTradelines,
        name="your-business-tradelines",
    ),
    path(
        "add-business-tradelines",
        views.AddBusinessTradelines,
        name="add-business-tradelines",
    ),
    path("dispute", views.DisputeView, name="dispute"),
    path(
        "update-company-information",
        views.UpdateCompanyInformation,
        name="update-company-information",
    ),
    path(
        "business-credit-reports",
        views.BusinessCreditReports,
        name="business-credit-reports",
    ),
    path(
        "current-business-tradelines",
        views.CurrentBusinessTradelines,
        name="current-business-tradelines",
    ),
]
