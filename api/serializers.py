from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'owner']


class StudentSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Student
        fields = ['fullName', 'email', 'sex', 'matric_no', 'image', 'date_created', 'owner']

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def put(self, instance, validated_data):
        instance.fullName = Student('fullName', instance.fullName)
        instance.email = Student('email', instance.email)
        instance.sex = Student('sex', instance.sex)
        instance.matric_no = Student('matric_no', instance.matric_no)

        if instance.is_valid():
            instance.save()
            return instance
