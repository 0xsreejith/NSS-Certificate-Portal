from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='certificates/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Certificate for {self.student.user.username}"
