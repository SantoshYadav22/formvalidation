from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    Name=serializers.CharField(max_length=100)
    Age=serializers.IntegerField()
    Email=serializers.EmailField(max_length=100)
    Place=serializers.CharField(max_length=100)
    Password=serializers.CharField(max_length=100,default='not available')
    ReEnterPassword=serializers.CharField(max_length=100,default='not available')
