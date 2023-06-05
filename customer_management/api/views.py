from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import JobSerializer,PartFullFormSerializer
from myapp.models import Job,PartFullForm,Air_craft,User,PartNumber
# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def create(self, request, *args, **kwargs):
        job_data = request.data
        part_forms_data = job_data.pop('parts', [])  # Remove 'parts' from job_data
        j_name=job_data.get('customer')
        a_name=job_data.get('air_craft')
        j_obj=User.objects.get(username=j_name)
        a_obj=Air_craft.objects.get(air_craft_name=a_name)
        job_serializer = self.get_serializer(data=job_data)
        job_serializer.is_valid(raise_exception=True)

        job = job_serializer.save(customer=j_obj,air_craft=a_obj)

        part_forms = []
        for part_form_data in part_forms_data:
            part_form_data['job'] = job.id
            part_form_serializer = PartFullFormSerializer(data=part_form_data)
            part_form_serializer.is_valid(raise_exception=True)
            part_form = part_form_serializer.save()
            part_forms.append(part_form)

        response_data = job_serializer.data
        response_data['parts'] = PartFullFormSerializer(part_forms, many=True).data

        headers = self.get_success_headers(response_data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        # context={
        #     'air_craft':Air_craft.objects.all(),
        #     'users':User.objects.all(),
        #     'parts':PartNumber.objects.all(),
        #     'response_data':response_data

        # }
        # return render(request,'job_create.html',context)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return render(request, 'job_list.html', {'jobs': serializer.data})



class PartFullFormViewSet(viewsets.ModelViewSet):
    queryset = PartFullForm.objects.all()
    serializer_class = PartFullFormSerializer


  