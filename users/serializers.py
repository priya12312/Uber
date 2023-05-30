from rest_framework import serializers
from users.models import *

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class StudentsAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentsAddress
        fields = '__all__'

class StudentDetailsAddressSerializers(serializers.ModelSerializer):
    students_address = StudentsAddressSerializers(many=True)
    class Meta:
        model = Students
        fields = ('name','surname','birth','mobile','students_address')





