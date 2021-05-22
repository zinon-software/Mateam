# rest framewoark
### get data form model ---> json

from rest_framework import serializers
from app.models import Customer

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
