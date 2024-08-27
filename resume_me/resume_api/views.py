from rest_framework import viewsets
from .models import User, Resume, TailoredResume
from .serializers import UserSerializer, ResumeSerializer, TailoredResumeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class TailoredResumeViewSet(viewsets.ModelViewSet):
    queryset = TailoredResume.objects.all()
    serializer_class = TailoredResumeSerializer