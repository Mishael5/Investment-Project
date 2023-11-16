from django.urls import path
from dashboard import views

urlpatterns = [
    # path('about/', views.about, name='about'),
    # Add other URL patterns as needed
    path('login_required/', views.user_dashboard, name='dashboard'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('investment_profile/', views.investment_profile, name='investment_profile'),
    path('agrovest/', views.agrovest, name='agrovest'),
    path('construction/', views.construction, name='construction'),
    path('E_trading/', views.E_trading, name='E_trading'),
    path('Eduvest/', views.Eduvest, name='Eduvest'),
    path('lpg/', views.lpg, name='lpg'),
    path('Medicals/', views.Medicals, name='Medicals'),
    path('cleaning/', views.cleaning, name='cleaning'),
    path('cosmetology/', views.cosmetology, name='cosmetology'),
    path('cosmetology/', views.cosmetology, name='cosmetology'),
    path('sports/', views.sports, name='sports'),
    path('Realestate/', views.Realestate, name='Realestate'),

]
