from rest_framework import serializers
from accounts.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fullname','email','website', 'phone']
