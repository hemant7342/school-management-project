from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('principal', 'principal'),
        ('teacher', 'teacher'),
        ('student', 'student'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"

    class Meta:
        db_table = "users"   # ✅ phpMyAdmin table name
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["id"]


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column="user_id")
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=20)
    roll_no = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.class_name})"

    class Meta:
        db_table = "students"
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["roll_no"]


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column="user_id")
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        db_table = "teachers"
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        ordering = ["name"]


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column="student_id")
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.marks}"

    class Meta:
        db_table = "results"
        verbose_name = "Result"
        verbose_name_plural = "Results"
        ordering = ["student", "subject"]
