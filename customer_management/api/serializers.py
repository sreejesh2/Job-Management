from myapp.models import Job,PartFullForm,PartNumber,Air_craft
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class AirCraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Air_craft
        fields = ['id', 'air_craft_name']



class PartNumberSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    model=PartNumber
    fields="__all__"


class PartFullFormSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=PartFullForm
        fields="__all__"

class JobSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    part_numbers=serializers.CharField(read_only=True)
    parts=PartFullFormSerializer(read_only=True,many=True)
    customer = serializers.SerializerMethodField()
    air_craft = serializers.SerializerMethodField()

    def get_customer(self, obj):
        customer = obj.customer
        if customer:
            return customer.username
        return None
    def get_air_craft(self, obj):
        air_craft = obj.air_craft
        if air_craft:
            return air_craft.air_craft_name
        return None   
     
    class Meta:
        model=Job
        fields=["id","job_number","customer","air_craft","work_details","note","po_number","po_image","part_numbers","parts"]
