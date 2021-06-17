from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home-page'),
    path('donate',views.donate),
    path('creditcard',views.credit),
    path('debitcard',views.debit),
    path('creditcard1',views.createcredit),
    path('debitcard1',views.createdebit),
    path('otp',views.createcreditotp),
    path('otp1',views.createdebitotp)

]