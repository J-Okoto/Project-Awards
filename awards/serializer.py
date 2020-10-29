from rest_framework import serializers
from .models import Profile,Project,Countries

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields='__all__'

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields='__all__'