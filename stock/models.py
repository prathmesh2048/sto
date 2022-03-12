from statistics import mode
from django.db import models



class RegistrationFormDemant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    DOB = models.CharField(max_length=50)
    PAN_Number = models.CharField(max_length=50)
    bank_acc_number = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    adhar_number = models.CharField(max_length=50)
    created = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

class stock(models.Model):
    stock_name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    buy_price = models.CharField(max_length=50)
    sell_price = models.CharField(max_length=50)
    buy_date = models.CharField(max_length=50)
    sell_date = models.CharField(max_length=50)

    def __str__(self):
        return self.stock_name

class fund(models.Model):
    fund_balance = models.CharField(max_length=50)
    last_transaction_date = models.CharField(max_length=50)

    def __str__(self):
        return self.fund_balance
