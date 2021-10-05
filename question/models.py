from django.db import models
from course.models import Course
# Create your models here.






class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    text= models.TextField(max_length=1000)
    option_one=models.CharField(max_length=100)
    option_two=models.CharField(max_length=100)
    option_three=models.CharField(max_length=100)
    option_four=models.CharField(max_length=100)
    answer=models.IntegerField()
    time_created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text[:20 ]