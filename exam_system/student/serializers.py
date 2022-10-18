from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    phone_number = PhoneNumberField(region="IN")
    email = serializers.EmailField(max_length=254)
    active = serializers.BooleanField(default = True)
    PRN = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.PRN = validated_data.get('roll_no', instance.PRN)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    class Meta:
        model = Student
        fields = '__all__'

    