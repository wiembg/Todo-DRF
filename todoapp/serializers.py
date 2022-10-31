from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class TaskSerializer(serializers.ModelSerializer):
        owner = serializers.ReadOnlyField(source='owner.username')
        class Meta:
            model = Task
            fields = '__all__'
        def create(self, validated_data):
            return Task.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.completed = validated_data.get('completed', instance.completed)
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance


#building RESTful apis
#serializer : process of translating data structure or object state in the format that can be stored or transmitted ad reconstructred later
#:alloww complex data such as querysets and model instances to be converted from one form to other Form (generally JSON)
#serializer: responsible for converting objects into data types understandable by javascript and front-end frameworks.