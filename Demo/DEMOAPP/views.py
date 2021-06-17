import math, random
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.db import connection
from django.http import HttpResponse

from .models import Post, PostDebit, creditotp1,debitotp1


# Create your views here.
def home(request):
    return render(request, 'index.html')


def donate(request):
    return render(request, 'donate.html')


def credit(request):
    return render(request, 'credit.html')


def debit(request):
    return render(request, 'debit.html')


def createcredit(request):
    digits = "0123456789"
    OTP = ""
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('email') and request.POST.get('address') and request.POST.get('city') and request.POST.get('state') and request.POST.get('pincode') and request.POST.get('cardname') and request.POST.get('cardnumber') and request.POST.get('expmonth') and request.POST.get('expyear') and request.POST.get('cvv') and request.POST.get('amount'):
            post = Post()
            post.firstname = request.POST.get('firstname')
            post.email = request.POST.get('email')
            post.address = request.POST.get('address')
            post.city = request.POST.get('city')
            post.state = request.POST.get('state')
            post.pincode = request.POST.get('pincode')
            post.cardname = request.POST.get('cardname')
            post.cardnumber = request.POST.get('cardnumber')
            post.expmonth = request.POST.get('expmonth')
            post.expyear = request.POST.get('expyear')
            post.cvv = request.POST.get('cvv')
            post.amount = request.POST.get('amount')
            request.session['id'] = post.amount
            request.session['cid'] = post.email
            post.save()
            for i in range(4):
                OTP += digits[math.floor(random.random() * 10)]
            request.session['oid'] = OTP
            subject = "SPARK FOUNDATION"
            mail = post.email
            mail = EmailMessage(subject, OTP,
                                "Here is Your OTP",
                                to=[mail])
            mail.send()
            return render(request, 'credit1.html')


def createdebit(request):
    digits = "0123456789"
    OTP = ""
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('email') and request.POST.get('address') and request.POST.get('city') and request.POST.get('state') and request.POST.get('pincode') and request.POST.get('cardname') and request.POST.get('cardnumber') and request.POST.get('expmonth') and request.POST.get('expyear') and request.POST.get('cvv') and request.POST.get('amount'):
            post = PostDebit()
            post.firstname = request.POST.get('firstname')
            post.email = request.POST.get('email')
            post.address = request.POST.get('address')
            post.city = request.POST.get('city')
            post.state = request.POST.get('state')
            post.pincode = request.POST.get('pincode')
            post.cardname = request.POST.get('cardname')
            post.cardnumber = request.POST.get('cardnumber')
            post.expmonth = request.POST.get('expmonth')
            post.expyear = request.POST.get('expyear')
            post.cvv = request.POST.get('cvv')
            post.amount = request.POST.get('amount')
            request.session['id1'] = post.amount
            request.session['cid1'] = post.email
            post.save()
            for i in range(4):
                OTP += digits[math.floor(random.random() * 10)]
            request.session['oid1'] = post.OTP
            subject = "SPARK FOUNDATION"
            mail = post.email
            mail = EmailMessage(subject, OTP,
                                "Here is Your OTP",
                                to=[mail])
            mail.send()
            return render(request, 'debit1.html')


def createcreditotp(request):
    f = 0
    mail = 'muthavarapusandy@gmail.com'
    if request.method == 'POST':
        if request.POST.get('otp'):
            post = creditotp1()
            post.otp = request.POST.get('otp')

            post.mail = request.session['cid']
            post.amount = request.session['id']
            post.ootp = request.session['oid']

            a = debitotp1.objects.raw('SELECT otp as id from dotp')
            for p in a:
                if p.id == post.otp:
                    f = 1
                    break
            if f == 0:
                if post.ootp == post.otp:

                    subject = "SPARK FOUNDATION"
                    amount1 = post.amount
                    mail = post.mail
                    mail = EmailMessage(subject,amount1,
                                    " has been transfered from your Account (Using Credit card) to PM CARES FUNDS sucessfully!",
                                    to=[mail])
                    mail.send()

                    post.save()

                    return render(request,'thanks.html')
                else:
                    return render(request,'rror.html')
            else:
                return render (request,'credit1.html')

def createdebitotp(request):
    f = 0
    mail = 'muthavarapusandy@gmail.com'
    if request.method == 'POST':
        if request.POST.get('otp'):
            post = debitotp1()
            post.otp = request.POST.get('otp1')
            post.mail = request.session['cid1']
            post.amount = request.session['id1']
            a = debitotp1.objects.raw('SELECT otp as id from dotp')
            for p in a:
                if p.id == post.otp:
                    f = 1
                    break
            if f == 0:
                if post.ootp == post.otp:

                    subject = "SPARK FOUNDATION"
                    amount1 = post.amount
                    mail = post.mail
                    mail = EmailMessage(subject,amount1,
                                    " has been transfered from your Account (Using Debit card) to PM CARES FUNDS sucessfully!",
                                    to=[mail])
                    mail.send()

                    post.save()

                    return render(request,'thanks.html')
                else:
                    return render(request,'error1.html')
            else:
                return render (request,'credit1.html')