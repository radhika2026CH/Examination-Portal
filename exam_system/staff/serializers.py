from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import Staff

class StaffSerializers(serializers.ModelSerializer):
    staff_name = serializers.CharField(max_length=100)
    phone_number = PhoneNumberField(region="IN")
    email = serializers.EmailField(max_length=254)
    active = serializers.BooleanField(default = True)

    def create(self, validated_data):
        return Staff.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.staff_name = validated_data.get('staff_name', instance.staff_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    class Meta:
        model = Staff
        fields = '__all__'
