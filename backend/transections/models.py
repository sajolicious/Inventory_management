from django.db import models
from inventory.models import stock
# Create your models here.
class User(models.Model):
      username=models.CharField(max_length=50)
      password=models.CharField(max_length=50)
class Suppliers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    notes = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)
def __str__(self):
    return self.name


class PurchaseBill(models.Model):
    bill=models.AutoField(primary_key=True)
    purchase_time=models.DateTimeField(auto_now=True)
    suppliers=models.ForeignKey(Suppliers,on_delete=models.CASCADE,related_name='purchase')
def __str__(self):
	    return "Bill no: " + str(self.bill)

class PurchaseItem(models.Model):
    bill=models.ForeignKey(PurchaseBill,on_delete=models.CASCADE,related_name='purchItem')
    stock = models.ForeignKey(stock, on_delete = models.CASCADE, related_name='purchaseitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

def __str__(self):
	    return "Bill no: " + str(self.bill.billno) + ", Item = " + self.stock.name

class PurchaseBillDetails(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete = models.CASCADE, related_name='purchasedetailsbillno')
    quantity = models.PositiveIntegerField()
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(default=0)

    def __str__(self):
	    return "Bill no: " + str(self.billno.billno)

#contains the sale bills made
class SaleBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    bin = models.CharField(max_length=15)

    def __str__(self):
	    return "Bill no: " + str(self.billno)

def get_items_list(self):
        return SaleItem.objects.filter(billno=self)
        
def get_total_price(self):
        saleitems = SaleItem.objects.filter(billno=self)
        total = 0
        for item in saleitems:
            total += item.totalprice
        return total

#contains the sale stocks made
class SaleItem(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete = models.CASCADE, related_name='salebillno')
    stock = models.ForeignKey(stock, on_delete = models.CASCADE, related_name='saleitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

    def __str__(self):
	    return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name

#contains the other details in the sales bill
class SaleBillDetails(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete = models.CASCADE, related_name='saledetailsbillno')
    quantity = models.PositiveIntegerField()
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(default=0)
    
    def __str__(self):
	    return "Bill no: " + str(self.billno.billno)