from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Lead

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

    def create(self, validated_data):
        print('...validated_data...', validated_data)
        return Lead.objects.create(**validated_data)
