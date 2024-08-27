from rest_framework import serializers
from .models import User, Resume, TailoredResume

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'created_at']

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'user', 'base_resume', 'experience_doc', 'created_at']

class TailoredResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TailoredResume
        fields = ['id', 'user', 'resume', 'job_description', 'tailored_resume', 'created_at']