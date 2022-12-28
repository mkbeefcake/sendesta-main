from django.shortcuts import render , redirect
from django.contrib import messages
from users.models import UserProfile
from django.contrib.auth.decorators import login_required
from .models import (CompanyInformation
,YourBusinessRecommendation
,YourCurrentTradelines
,SendestaScore
,BusinessReports
,UpdateYourCompanyInformation,
Dispute)
from users.forms import UpdateProfileForm, UpdateUserForm
# Create your views here.

@login_required
def index(request):
  score = SendestaScore.objects.filter(user=request.user).first()
  recommendation = YourBusinessRecommendation.objects.filter(user=request.user)
  context = {}
  context['score'] = score
  context['recommendation'] = recommendation
  return render(request, 'dashboard/index.html',context)

@login_required
def Inbox(request):
  context = {}
  return render(request, 'dashboard/inbox.html',context)

@login_required
def Profile(request):
  context = {}
  user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
  
  context['form'] = UpdateUserForm(instance=request.user)
  context['profile_form'] = UpdateProfileForm(
        instance=request.user.userprofile)
  if request.method == 'POST':
      form = UpdateUserForm(request.POST, instance=request.user)
      profile_form = UpdateProfileForm(
            request.POST, instance=request.user.userprofile)
      if form.is_valid() and profile_form.is_valid():
          form.save()
          profile_form.save()
          messages.success(request, 'Your profile has been updated.')
          return redirect('profile')
      return redirect('profile')
  return render(request, 'dashboard/userprofile.html',context)

@login_required
def YourBusinessReport(request):
  context = {}
  reports = BusinessReports.objects.filter(user=request.user)
  context['reports'] = reports
  return render(request, 'dashboard/businessreports.html',context)

@login_required
def BusinessCreditReports(request):
  reports = BusinessReports.objects.filter(user=request.user)
  context = {}
  context['reports'] = reports
  score = SendestaScore.objects.filter(user=request.user).first()
  context['score'] = score
  company = CompanyInformation.objects.filter(user=request.user).first()
  context['company'] = company
  tradelines = YourCurrentTradelines.objects.filter(user=request.user)
  context['tradelines'] = tradelines
  return render(request, 'dashboard/yourbusinesscreditreport.html',context)

@login_required
def YourCompanyInformation(request):
  company = CompanyInformation.objects.filter(user=request.user).first()
  context = {}
  context['company'] = company
  return render(request, 'dashboard/yourcompanyinformation.html',context)

@login_required
def YourBusinessTradelines(request):
  tradelines = YourCurrentTradelines.objects.filter(user=request.user)
  context = {}
  context['tradelines'] = tradelines
  return render(request, 'dashboard/yourcurrentbusinesstradelines.html',context)

@login_required
def AddBusinessTradelines(request):
  tradelines = YourCurrentTradelines.objects.filter(user=request.user)
  context = {}
  context['tradelines'] = tradelines
  return render(request, 'dashboard/addbusinesstradelines.html',context)

@login_required
def DisputeView(request):
  context = {}
  if request.method == 'POST':
    business_name = request.POST.get('business_name')
    business_email = request.POST.get('business_email')
    business_phone = request.POST.get('business_phone')
    reason_of_dispute = request.POST.get('reason_of_dispute')
    Dispute.objects.create(
      business_name = business_name,
      business_email = business_email,
      business_phone = business_phone,
      reason_of_dispute = reason_of_dispute)
  tradelines = YourCurrentTradelines.objects.filter(user=request.user)
  context['tradelines'] = tradelines
  return render(request, 'dashboard/dispute.html',context)

@login_required
def UpdateCompanyInformation(request):
  context = {}
  company  = UpdateYourCompanyInformation.objects.filter(user=request.user).first()
  context['company'] = company
  return render(request, 'dashboard/updatecompanyinformation.html',context)


@login_required
def CurrentBusinessTradelines(request):
  context = {}
  tradelines = YourCurrentTradelines.objects.filter(user=request.user)
  context['tradelines'] = tradelines
  return render(request, 'dashboard/yourcurrentbusinesstradelines.html',context)

@login_required
def CancelMembership(request):
  request.user.userprofile.paid = False
  request.user.userprofile.save()
  return redirect('/dashboard/')

@login_required
def UpgradeMembership(request):
  return redirect('/')