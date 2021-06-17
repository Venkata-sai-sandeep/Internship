
from django.db import models

class Post(models.Model):
    firstname= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    cardname = models.CharField(max_length=100)
    cardnumber = models.CharField(max_length=100)
    expmonth = models.CharField(max_length=100)
    expyear = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    class Meta:
        db_table="credit"

class PostDebit(models.Model):
    firstname= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address =models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    cardname = models.CharField(max_length=100)
    cardnumber = models.CharField(max_length=100)
    expmonth = models.CharField(max_length=100)
    expyear = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    class Meta:
        db_table="debit"




class creditotp1(models.Model):
    otp = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    class Meta:
        db_table="cotp"

class debitotp1(models.Model):
    otp = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    class Meta:
        db_table="dotp"
