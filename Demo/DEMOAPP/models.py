

from django.db import models

class Post(models.Model):
    customerid = models.CharField(max_length=100)
    accountno = models.CharField(max_length=100)
    atmcardno =models.CharField(max_length=100)
    expiremonth = models.CharField(max_length=100)
    expireyear = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    passw = models.CharField(max_length=100)

    class Meta:
        db_table="signup1"

class Log(models.Model):
    cid = models.CharField(max_length=100)
    passw = models.CharField(max_length=100)

    class Meta:
        db_table="login"

class Mobilerecharge(models.Model):
    mobileno = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    plans = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table="mobilerecharge"

class Fastagrecharge(models.Model):
    banks = models.CharField(max_length=100)
    vehiclereg = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table="fastag"

class cableTvrecharge(models.Model):
    ctv = models.CharField(max_length=100)
    customerid = models.CharField(max_length=100)
    plans = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table="cabletv"

class Broadband(models.Model):
    network = models.CharField(max_length=100)
    customerid = models.CharField(max_length=100)
    plans = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table="broadband"


class Electricbills(models.Model):
    network = models.CharField(max_length=100)
    serviceno = models.CharField(max_length=100)
    ownername = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table="electricbills"


class Educationfee(models.Model):
    state = models.CharField(max_length=100)
    collage = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    feetype = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    collageid = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)
    class Meta:
        db_table="educationfee"


class Postpaid(models.Model):
    mobileno = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    plans = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)
    class Meta:
        db_table="postpaid"

class Donateoxygen(models.Model):
    amount = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)
    class Meta:
        db_table="donateoxygen"

class Applyhomelaonbank(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)
    class Meta:
        db_table="homeloan1"

class Applyeducationlaonbank(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    studyplace = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)
    class Meta:
        db_table="educationloan1"

class Applyvehiclelaonbank(models.Model):
    name = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    vehicletype = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)
    class Meta:
        db_table="vehicleloan1"

class Applyacountotacount(models.Model):
    accountnum = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    accountHoldername = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)
    class Meta:
        db_table="accounttoaccount1"


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)
    class Meta:
        db_table="contactus"

class Post3(models.Model):
    customerid = models.CharField(max_length=100,primary_key = True)
    accountno = models.CharField(max_length=100)
    adharno = models.CharField(max_length=100)
    atmcardno =models.CharField(max_length=100)
    expiremonth = models.CharField(max_length=100)
    expireyear = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    passw = models.CharField(max_length=100)
    class Meta:
        db_table="signup2"

class Applyloan(models.Model):
    name = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table="applyloan"


class Applylifeinsurance(models.Model):
    name = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    employeetype = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table = "lifeinsurance"

class Applyvehicleinsurance(models.Model):
    name = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    employeetype = models.CharField(max_length=100)
    vehicletype = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table = "vehicleinsurance"

class Makepayments(models.Model):
    name = models.CharField(max_length=100)
    cardnumber = models.CharField(max_length=100)
    expirydate = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table = "payments"


class Makepayments1(models.Model):
    name = models.CharField(max_length=100)
    cardnumber = models.CharField(max_length=100)
    expirydate = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)

    class Meta:
        db_table = "payments1"
