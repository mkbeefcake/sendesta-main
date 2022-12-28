from django.urls import path
from . import views

urlpatterns = [
  path('',views.Index,name='index'),
  path('business/',views.BusinessServices,name='business'),
  path('legal/',views.Legal,name='legal'),
  path('contact/',views.Contact,name='contact'),
  path('about/',views.About,name='about'),
  path('account',views.Account,name='account'),
  path('register/<int:id>/',views.AccountWithPay,name='register'),
  path('make_payment/<int:id>/',views.MakePaymentView,name='make_payment'),
  path('config/', views.stripe_config),
  path('success/', views.Success),
  path('create-checkout-session/<int:id>/', views.MakePayment),
]
