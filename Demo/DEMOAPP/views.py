from django.shortcuts import render
from django.core.mail import EmailMessage
from django.db import connection
from django.http import HttpResponse
from .models import Post, Log, Mobilerecharge, Fastagrecharge, cableTvrecharge, Broadband, Electricbills, \
    Educationfee, Postpaid, Donateoxygen, Applyhomelaonbank, Applyeducationlaonbank, Applyvehiclelaonbank, \
    Applyacountotacount, Contact, Applyloan, Applylifeinsurance, Applyvehicleinsurance, Post3, Makepayments, \
    Makepayments1


# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')
def history(request):
    return render(request,'history.html')
def signup(request):
    return render(request,'signup.html')
def aboutus(request):
    return render(request,'ourteam.html')
def contactus(request):
    return render(request,'contactus.html')
def netbanking(request):
    return render(request,'netbanking.html')
def netbanking1(request):
    return render(request,'netbanking1.html')
def netbankingoperations(request):
    return render(request,'netbankingoperations.html')
def netbankingregister(request):
    return render(request,'netbankingregister.html')
def personalbanking(request):
    return render(request,'personalbanking.html')
def personalbanking1(request):
    return render(request,'personalbanking1.html')
def pesronalbankingoperations(request):
    return render(request,'personalbankingoperations.html')
def vehicleloan(request):
    return render(request,'vehicleloan.html')
def educationloan(request):
    return render(request,'educationloan.html')
def homeloan(request):
    return render(request,'homeloan.html')
def home1(request):
    return render(request,'home1.html')
def lifeinsurance(request):
    return render(request,'lifeincurence.html')
def healthinsurance(request):
    return render(request,'healthinsurance.html')
def vehicleinsurance(request):
    return render(request,'vehicleinsurance.html')
def mobilerecharge(request):
    return render(request,'mobilerecharge.html')
def educationfee(request):
    return render(request,'educationfee.html')
def mywallet(request):
    return render(request,'mywallet.html')
def fastag(request):
    return render(request,'fastag.html')
def fixeddeposits(request):
    return render(request,'fixeddiposits.html')
def cabletv(request):
    return render(request,'cabletv.html')
def broadband(request):
    return render(request,'broadband.html')
def postpaid(request):
    return render(request,'postpaid.html')
def electricitybills(request):
    return render(request,'electricitybills.html')
def donateoxygen(request):
    return render(request,'donateoxygen.html')
def applyloans(request):
    return render(request,'applyloans.html')
def applyloans1(request):
    return render(request,'applyloan1.html')
def insurance(request):
    return render(request,'insurance.html')
def insurance1(request):
    return render(request,'insurance1.html')
def accounttransaction(request):
    return render(request,'accounttransaction.html')

def createpost(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('customerid') and request.POST.get('accountno') and request.POST.get('adharno') and request.POST.get('atmcardno') and request.POST.get('expiremonth') and request.POST.get('expireyear')and request.POST.get('mobileno')and request.POST.get('mail')and request.POST.get('cvv')and request.POST.get('passw') :
            post = Post3()
            post.customerid = request.POST.get('customerid')
            post.accountno = request.POST.get('accountno')
            post.adharno = request.POST.get('adharno')
            post.atmcardno = request.POST.get('atmcardno')
            post.expiremonth = request.POST.get('expiremonth')
            post.expireyear = request.POST.get('expireyear')
            post.mobileno = request.POST.get('mobileno')
            post.mail = request.POST.get('mail')
            post.cvv = request.POST.get('cvv')
            post.passw = request.POST.get('passw')
            a = Post3.objects.raw('SELECT customerid,mobileno,accountno from signup2')
            for p in a:
                if p.customerid == post.customerid or p.mobileno == post.mobileno or p.accountno == post.accountno:
                    f = 1
                    break
            if (f == 1):
                return render(request, 'home1.html')
            else:
                post.save()
                subject = "VNS BANK"
                mail = post.mail
                mail = EmailMessage(subject,
                                     "Welcome to VNS ONLINE BANKING AND FINANCE SERVICES (INDIAS ONE OF THE SAFEEST site) to get fast and secure transactions-regards Team VNS ",
                                     to=[mail])
                mail.send()
                return render(request, 'login.html')
        else:
            return render(request, 'home.html')
            post.save()
            return render(request, 'login.html')
    else:
        return render(request, 'home.html')

def createlogin(request):
    f=0
    if request.method == 'POST':
      if request.POST.get('cid') and request.POST.get('passw'):
            l=Log()
            l.cid=request.POST.get('cid')
            l.passw=request.POST.get('passw')
            a=Post3.objects.raw('SELECT customerid ,passw from signup2')
            for p in a:
                if p.customerid == l.cid and  p.passw == l.passw:
                    f=1
                    break
            if(f==1):
                l.save()
                return render(request,'home1.html')
            else:
                return render(request, 'signup.html')
    else:
        return render(request, 'home.html')



def createmobilerecharge(request):
    f=0
    if request.method == 'POST' :
        if request.POST.get('mobileno') and request.POST.get('network') and request.POST.get('state') and request.POST.get('plans') and request.POST.get('mail') and request.POST.get('cid') :
            post = Mobilerecharge()
            post.mobileno = request.POST.get('mobileno')
            post.network = request.POST.get('network')
            post.state = request.POST.get('state')
            post.plans = request.POST.get('plans')
            post.mail = request.POST.get('mail')
            post.cid = request.POST.get('cid')
            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid :
                    f=1
                    break
            if f==1:
                post.save()
                return render(request,'payments.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')

def createfastag(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('banks') and request.POST.get('vehiclereg') and request.POST.get('amount') and request.POST.get('mail') and request.POST.get('cid'):
            post = Fastagrecharge()
            post.banks = request.POST.get('banks')
            post.vehiclereg = request.POST.get('vehiclereg')
            post.amount = request.POST.get('amount')
            post.mail = request.POST.get('mail')
            post.cid = request.POST.get('cid')
            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'payments.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')

def createcabletv(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('ctv') and request.POST.get('customerid') and request.POST.get('plans') and request.POST.get('mail') and request.POST.get('cid') :
            post = cableTvrecharge()
            post.ctv = request.POST.get('ctv')
            post.customerid = request.POST.get('customerid')
            post.plans = request.POST.get('plans')
            post.mail =  request.POST.get('mail')
            post.cid = request.POST.get('cid')
            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'payments.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')

def createbroadband(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('network') and request.POST.get('customerid') and request.POST.get('plans') and request.POST.get('mail') and request.POST.get('cid') :
            post = Broadband()
            post.network = request.POST.get('network')
            post.customerid = request.POST.get('customerid')
            post.plans = request.POST.get('plans')
            post.mail =  request.POST.get('mail')
            post.cid = request.POST.get('cid')
            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'payments.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')


def createelectricbills(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('network') and request.POST.get('serviceno') and request.POST.get('ownername') and request.POST.get('amount') and request.POST.get('mail') and request.POST.get('cid') :
            post = Electricbills()
            post.network = request.POST.get('network')
            post.serviceno = request.POST.get('serviceno')
            post.ownername = request.POST.get('ownername')
            post.amount = request.POST.get('amount')
            post.mail =  request.POST.get('mail')
            post.cid = request.POST.get('cid')
            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'payments.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')


def createeducationfee(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('state') and request.POST.get('collage') and request.POST.get('year') and request.POST.get('semester') and request.POST.get('feetype') and request.POST.get('amount') and request.POST.get('collageid')and request.POST.get('mail') and request.POST.get('cid') :
            post = Educationfee()
            post.state = request.POST.get('network')
            post.collage = request.POST.get('customerid')
            post.year = request.POST.get('plans')
            post.semester = request.POST.get('cid')
            post.feetype = request.POST.get('feetype')
            post.amount = request.POST.get('amount')
            post.collageid = request.POST.get('collageid')
            post.mail =  request.POST.get('mail')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request, 'payments.html')

            else:
                return render(request, 'educationfee.html')

        else:
            return render('home.html')

def createeducationfee1(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('state') and request.POST.get('collage') and request.POST.get('year') and request.POST.get('semester') and request.POST.get('feetype') and request.POST.get('amount') and request.POST.get('collageid')and request.POST.get('mail') and request.POST.get('cid') :
            post = Educationfee()
            post.state = request.POST.get('state')
            post.collage = request.POST.get('collage')
            post.year = request.POST.get('year')
            post.semester = request.POST.get('semester')
            post.feetype = request.POST.get('feetype')
            post.amount = request.POST.get('amount')
            post.collageid = request.POST.get('collageid')
            post.mail =  request.POST.get('mail')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'payments.html')
            else:
                return render(request,'educationfee.html')

        else:
            return render(request,'home.html')



def createpostpaid(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('mobileno') and request.POST.get('network') and request.POST.get('plans') and request.POST.get('mail') and  request.POST.get('cid') :
            post = Postpaid()
            post.mobileno = request.POST.get('mobileno')
            post.network = request.POST.get('network')
            post.plans = request.POST.get('plans')
            post.mail =  request.POST.get('mail')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'payments.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')


def createdonateoxygen(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('amount') and request.POST.get('mail') and request.POST.get('cid') :
            post = Donateoxygen()
            post.amount = request.POST.get('amount')
            post.mail = request.POST.get('mail')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'payments1.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')


def createhomeloan1(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('mobileno') and request.POST.get('email') and request.POST.get('city') and request.POST.get('amount') and request.POST.get('years') and request.POST.get('cid'):
            post = Applyhomelaonbank()
            post.fname = request.POST.get('fname')
            post.lname = request.POST.get('lname')
            post.mobileno = request.POST.get('mobileno')
            post.email = request.POST.get('email')
            post.city = request.POST.get('city')
            post.amount = request.POST.get('amount')
            post.years = request.POST.get('years')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                subject = "VNS BANK"
                mail = post.email
                mail = EmailMessage(subject,
                                    "Welcome to VNS ONLINE BANKING AND FINANCE SYSTEM (INDIAS ONE OF THE FASTEST site) to get safe and secure transactions-regards Team VNS .Thanks for Your Intrest towards our VNS Banking and Finance.Our representative weill meet you Soon .STAY HOME - STAY SAFE",
                                    to=[mail])
                mail.send()
                return render(request,'homeloan1.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')



def createeducationloan1(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('mobileno') and request.POST.get('email') and request.POST.get('city') and request.POST.get('studyplace') and request.POST.get('amount') and request.POST.get('cid'):
            post = Applyeducationlaonbank()
            post.fname = request.POST.get('fname')
            post.lname = request.POST.get('lname')
            post.mobileno = request.POST.get('mobileno')
            post.email = request.POST.get('email')
            post.city = request.POST.get('city')
            post.studyplace = request.POST.get('studyplace')
            post.amount = request.POST.get('amount')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                subject = "VNS BANK"
                mail = post.email
                mail = EmailMessage(subject,
                                    "Welcome to VNS ONLINE BANKING AND FINANCE SYSTEM (INDIAS ONE OF THE FASTEST site) to get safe and secure transactions-regards Team VNS .Thanks for Your Intrest towards our VNS Banking and Finance.Our representative weill meet you Soon .STAY HOME - STAY SAFE",
                                    to=[mail])
                mail.send()
                return render(request,'educationloan1.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')

def createvehicleloan1(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('mobileno') and request.POST.get('vehicletype') and request.POST.get('amount') and request.POST.get('years') and request.POST.get('cid'):
            post = Applyvehiclelaonbank()
            post.name = request.POST.get('name')
            post.mobileno = request.POST.get('mobileno')
            post.vehicletype = request.POST.get('vehicletype')
            post.amount = request.POST.get('amount')
            post.years = request.POST.get('years')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'vehicleloan1.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')

def createaccounttoaccount(request):
    if request.method == 'POST':
        if request.POST.get('accountnum') and request.POST.get('ifsc') and request.POST.get('accountHoldername') and request.POST.get('amount') and request.POST.get('cid'):
            post = Applyacountotacount()
            post.accountnum= request.POST.get('accountnum')
            post.ifsc = request.POST.get('ifsc')
            post.accountHoldername = request.POST.get('accountHoldername')
            post.amount = request.POST.get('amount')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'accounttransaction1.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')

def createcontactus(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('state') and request.POST.get('subject') :
            post = Contact()
            post.firstname = request.POST.get('firstname')
            post.lastname = request.POST.get('lastname')
            post.state = request.POST.get('state')
            post.subject = request.POST.get('subject')

            a = Log.objects.raw('SELECT cid as id from login')

            post.save()
            return render(request,'contact1.html')
        else:
            return render(request,'mobilerecharge2.html')

    else:
        return render('home.html')



def createapplyloan(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('mobileno') and request.POST.get('mail') and request.POST.get('city') and request.POST.get('income') and request.POST.get('type') and request.POST.get('cid'):
            post = Applyloan()
            post.name = request.POST.get('name')
            post.mobileno = request.POST.get('mobileno')
            post.mail = request.POST.get('mail')
            post.city = request.POST.get('city')
            post.income = request.POST.get('income')
            post.type = request.POST.get('type')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'applyloans2.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')

def createlifeinsurance(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('mobileno') and request.POST.get('gender') and request.POST.get('income') and request.POST.get('employeetype') and request.POST.get('cid') :
            post = Applylifeinsurance()
            post.name = request.POST.get('name')
            post.mobileno = request.POST.get('mobileno')
            post.gender = request.POST.get('gender')
            post.income = request.POST.get('income')
            post.employeetype = request.POST.get('employeetype')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'applyloans2.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')


def createvehicleinsurance(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('mobileno') and request.POST.get('gender') and request.POST.get('income') and request.POST.get('employeetype') and request.POST.get('vehicletype') and request.POST.get('cid') :
            post = Applyvehicleinsurance()
            post.name = request.POST.get('name')
            post.mobileno = request.POST.get('mobileno')
            post.gender = request.POST.get('gender')
            post.income = request.POST.get('income')
            post.employeetype = request.POST.get('employeetype')
            post.vehicletype = request.POST.get('vehicletype')
            post.cid = request.POST.get('cid')

            a = Log.objects.raw('SELECT cid as id from login')
            for p in a:
                if p.id == post.cid:
                    f = 1
                    break
            if f == 1:
                post.save()
                return render(request,'applyloans2.html')
            else:
                return render(request,'mobilerecharge2.html')

        else:
            return render('home.html')


def mobilerechargepayment(request):
    f=0
    mail=None
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('cardnumber') and request.POST.get('expiredate') and request.POST.get('cvv') and request.POST.get('cid') :
            post = Makepayments()
            post.name = request.POST.get('name')
            post.cardnumber = request.POST.get('cardnumber')
            post.expiredate = request.POST.get('expirydate')
            post.cvv = request.POST.get('cvv')
            post.cid = request.POST.get('cid')
            a = Log.objects.raw('SELECT mail as mail from mobilerecharge')

            subject = "VNS BANK"
            mail = EmailMessage(subject,
                                "Welcome to VNS ONLINE BANKING AND FINANCE SYSTEM (INDIAS ONE OF THE FASTEST site) to get safe and secure transactions-regards Team VNS .Thanks for Your Intrest towards our VNS Banking and Finance.Our representative weill meet you Soon .STAY HOME - STAY SAFE",
                                to=[mail])
            mail.send()



            return render(request,'fastag1.html')
        else:
            return render(request,'mobilerecharge2.html')

    else:
        return render(request,'home.html')


def oxygendonapepayment(request):
    f=0
    mail=None
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('cardnumber') and request.POST.get('expiredate') and request.POST.get('cvv') and request.POST.get('cid') :
            post = Makepayments1()
            post.name = request.POST.get('name')
            post.cardnumber = request.POST.get('cardnumber')
            post.expiredate = request.POST.get('expirydate')
            post.cvv = request.POST.get('cvv')
            post.cid = request.POST.get('cid')
            a = Log.objects.raw('SELECT mail as mail from mobilerecharge')

            subject = "VNS BANK"
            mail = EmailMessage(subject,
                                "Welcome to VNS ONLINE BANKING AND FINANCE SYSTEM (INDIAS ONE OF THE FASTEST site) to get safe and secure transactions-regards Team VNS .Thanks for Your Intrest towards our VNS Banking and Finance.Our representative weill meet you Soon .STAY HOME - STAY SAFE",
                                to=[mail])
            mail.send()



            return render(request,'donateoxygen1.html')
        else:
            return render(request,'mobilerecharge2.html')

    else:
        return render(request,'home.html')

