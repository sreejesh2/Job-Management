from django.db import models
from django.contrib.auth.models import User
from django.forms import inlineformset_factory


from django.db import models
from django.contrib.auth.models import User


class Air_craft(models.Model):
    air_craft_name = models.CharField(max_length=100, unique=True)


class PartNumber(models.Model):
    number = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.number


class Job(models.Model):
    job_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    air_craft = models.ForeignKey(
        Air_craft, on_delete=models.SET_NULL, null=True, blank=True)
    work_details = models.TextField(max_length=300, null=True, blank=True)
    note = models.TextField(max_length=500, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    po_number = models.CharField(max_length=200, null=True, blank=True)
    po_image = models.ImageField(upload_to='po_images', null=True, blank=True)
    part_numbers = models.ManyToManyField(
        PartNumber, through='PartFullForm', blank=True)


    def __str__(self):
        return self.job_number
    
    


class PartFullForm(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    part_number = models.ForeignKey(PartNumber, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    tsn = models.CharField(max_length=100, null=True, blank=True)
    tso = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Part: {self.part_number}, Job: {self.job}"
    

