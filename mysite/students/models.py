from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

grade_values = [
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
]

mark_validator = [
    MinValueValidator(0), MaxValueValidator(100)
]
help_text = "Mark should be between 0 and 100"

subject_list = [
    ('English', 'English'),
    ('German', 'German'),
    ('Science', 'Science'),
    ('Social Studies', 'Social Studies'),
    ('Math', 'Math'),
    ('Ethics', 'Ethics'),
]

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=2, choices=grade_values)
    dob = models.DateField('Date of Birth')

    def __str__(self) -> str:
        return self.name


class Marksheet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30, choices=subject_list)
    mark = models.PositiveIntegerField(
        validators=mark_validator, help_text=help_text, default=0
    )

    def __str__(self) -> str:
        return self.subject
            




