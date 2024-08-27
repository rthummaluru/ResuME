from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    base_resume = models.FileField(upload_to='base_resumes/')
    experience_doc = models.FileField(upload_to='experience_docs/')
    created_at = models.DateTimeField(auto_now_add=True)

class TailoredResume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_description = models.TextField()
    tailored_resume = models.FileField(upload_to='tailored_resumes/')
    created_at = models.DateTimeField(auto_now_add=True)