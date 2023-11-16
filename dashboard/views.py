from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def user_dashboard(request):
    # Add context data here if needed
    return render(request, 'dashboard/index.html')


@login_required(login_url='/accounts/login/')
def investment_profile(request):
    return render(request, 'dashboard/investment-profile.html')


@login_required(login_url='/accounts/login/')
def agrovest(request):
    return render(request, 'dashboard/agrovest.html')


@login_required(login_url='/accounts/login/')
def construction(request):
    return render(request, 'dashboard/construction.html')


@login_required(login_url='/accounts/login/')
def E_trading(request):
    return render(request, 'dashboard/E_trading.html')


@login_required(login_url='/accounts/login/')
def Eduvest(request):
    return render(request, 'dashboard/Eduvest.html')


@login_required(login_url='/accounts/login/')
def lpg(request):
    return render(request, 'dashboard/lpg.html')


@login_required(login_url='/accounts/login/')
def Medicals(request):
    return render(request, 'dashboard/medicals.html')


@login_required(login_url='/accounts/login/')
def cleaning(request):
    return render(request, 'dashboard/cleaning.html')


@login_required(login_url='/accounts/login/')
def cosmetology(request):
    return render(request, 'dashboard/cosmetology.html')



@login_required(login_url='/accounts/login/')
def sports(request):
    return render(request, 'dashboard/sports.html')



@login_required(login_url='/accounts/login/')
def Realestate(request):
    return render(request, 'dashboard/Realestate.html')





