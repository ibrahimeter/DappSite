from django.db import models

# Create your models here.
class Maintenance(models.Model):
    unit = models.CharField(max_length=5, blank=1, null=True, choices=[('GT1','GT1'),('GT2', 'GT2'),('ST', 'ST')] )
    MainDesc = models.CharField(max_length=100, blank=True, null=True)
    EOH = models.DecimalField(decimal_places=4, max_digits=10, blank=True, null=True)
    MainDate = models.DateField(null=True)
    Firm = models.CharField(max_length=100, blank= True, null=True)
 

class AnnualReport(models.Model):
    title = models.CharField(max_length=100, null='true', default='Annual Operation Report')
    pdffile = models.FileField(upload_to='annualreport/')
