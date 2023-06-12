from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(models.Model):
    class_no = models.CharField(max_length=2)  # 班别，如 "1A"
    student_no = models.IntegerField()         # 学号
    unique_id = models.CharField(max_length=10, unique=True)  # 学生独一无二的编号
    last_login = models.DateTimeField(null=True)  # 添加 last_login 字段

    USERNAME_FIELD = 'unique_id'
    REQUIRED_FIELDS = ['class_no', 'student_no']

    def __str__(self):
        return f"{self.class_no}{self.student_no}"

    @property
    def email(self):
        return f"{self.unique_id}@ylcss.edu.hk"

class Crush(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="crushes")
    crush = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admirers")
    matched = models.BooleanField(default=False)  # 标记是否配对成功

    def __str__(self):
        return f"{self.user} -> {self.crush}"
