from rest_framework import serializers
from .models import *

 # Validators
def notUpperCase(value):
    if value != value.lower():
        raise serializers.ValidationError('Name Must be in Lowercase Not Uppercase')
    return value

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields= ['name', 'roll']                        #Validate
        # extra_kwargs = {'roll':{'read_only':True}}                #Validate

# class StudentSerializers(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[notUpperCase])
#     roll = serializers.CharField(max_length=100)
#     city = serializers.CharField(max_length=100)
#     created_dt = serializers.DateTimeField()

    # def create(self, validated_data):             
    #     return Student.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.created_dt = validated_data.get('created_dt', instance.created_dt)
    #     instance.save()
    #     return instance
    
    # Field level Validations
    def validate_name(self, value):
        if value != value.upper():
            raise serializers.ValidationError("Name Must be in upper case")
        return value
    
    # object level validations
    # def validate(self, data):
    #     name = data.get('name')
    #     if len(name) > 8:
    #         raise serializers.ValidationError("Name Length Must be only 8 Character")
    #     return  data
    
class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'
        # read_only_fields= ['name', 'roll']                        #Validate
        # extra_kwargs = {'roll':{'read_only':True}}