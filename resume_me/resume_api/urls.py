from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ResumeViewSet, TailoredResumeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'tailored-resumes', TailoredResumeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]