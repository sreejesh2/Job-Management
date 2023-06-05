from django.db import models
from django.contrib.auth.models import User
from django.forms import inlineformset_factory


from django.db import models
from django.contrib.auth.models import User


class Air_craft(models.Model):
    air_craft_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.air_craft_name


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
    
    @property
    def parts(self):
        return PartFullForm.objects.filter(job=self)
    
    @parts.setter
    def parts(self, new_parts):
        # Clear existing parts associated with the job
        self.partfullform_set.all().delete()
        
        # Create new PartFullForm instances based on the provided parts data
        for part_data in new_parts:
            part_number_name = part_data.get('part_number')
            part_number = PartNumber.objects.get(number=part_number_name)
            
            PartFullForm.objects.create(job=self, part_number=part_number, **part_data)
    
    @property
    def part_numbers(self):
        return ', '.join([part.part_number.number for part in self.parts.all()])

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
    

