from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Air_craft,Job,PartNumber,PartFullForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

# Create your views here.

def create_job(request):
    print(request.POST)
    if request.method == 'POST':
        job_number = request.POST.get('job_number')
        customer_id = request.POST['customer']
        air_craft_id = request.POST['air_craft']
        work_details = request.POST['work_details']
        po_number = request.POST['po_number']
        po_image = request.FILES.get('po_image')
        note = request.POST['note']

        # Create a new Job instance
        job = Job(job_number=job_number, work_details=work_details, po_number=po_number, note=note)

        # Set the customer and aircraft for the job
        job.customer_id = customer_id
        job.air_craft_id = air_craft_id

        # Save the job to the database
        job.save()

        part_numbers = request.POST.getlist('part_number')
        descriptions = request.POST.getlist('description')
        serial_numbers = request.POST.getlist('serial_number')
        tsns = request.POST.getlist('tsn')
        tsos = request.POST.getlist('tso')

        for i in range(len(part_numbers)):
            part_number_id = part_numbers[i]
            description = descriptions[i]
            serial_number = serial_numbers[i]
            tsn = tsns[i]
            tso = tsos[i]

            part_number = PartNumber.objects.get(id=part_number_id)

            # Create a PartFullForm instance
            part_full_form = PartFullForm.objects.create(
                job=job,
                part_number=part_number,
                description=description,
                serial_number=serial_number,
                tsn=tsn,
                tso=tso
            )

            # Save the PartFullForm instance to the database
            part_full_form.save()

            # Add the PartFullForm instance to the job's part_numbers relationship
            # job.part_numbers.add(part_full_form.id)

        return redirect('all-jobs')

    users = User.objects.all()
    air_craft = Air_craft.objects.all()
    parts = PartNumber.objects.all()
    return render(request, 'addjob.html', {'users': users, 'air_craft': air_craft, 'parts': parts})







def create_part(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        description = request.POST.get('description')
        
        part = PartNumber.objects.create(number=number, description=description)
        part.save()

        return redirect('add-job')  

    return render(request, 'addjob.html') 





