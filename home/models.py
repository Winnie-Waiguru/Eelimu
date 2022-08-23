from datetime import date
from django.db import models

# Create your models here.

class Visitor(models.Model):
    First_name= models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.EmailField
    Password=models.CharField(max_length=12)
    Age=models.SmallIntegerField()
    Location=models.CharField(max_length=30)
    Phone_number=models.CharField(max_length=15)
    Interests= models.CharField(max_length= 30)
    
class Student(models.Model):
    Student_image=models.ImageField()
    Roll_number=models.IntegerField()  
    Student_fullname=models.CharField(max_length=50, default=True)
    Student_email=models.EmailField()
    Student_phone_number=models.CharField(max_length=15)
    Student_location=models.CharField(max_length=30)
    Student_college=models.CharField(max_length=30)
    
class Course(models.Model):
    Course_id=models.CharField(max_length=20, primary_key= True)
    name=models.CharField(max_length=30)
    duration=models.CharField(max_length= 50)
    year=models.DateField()
    status=models.CharField(max_length=30)
    
class Schedule(models.Model):
    Schedule_id=models.CharField(max_length=40)
    date=models.DateField()  
    
class Trainer(models.Model):
    Trainer_id=models.CharField(max_length=10)
    Full_name=models.CharField(max_length=50)
    Trainers_picture=models.ImageField(null=True)
    Course=models.ForeignKey('Course', on_delete=models.CASCADE,related_name='Trainer_Course')
    Email=models.EmailField()
    Phone_number=models.CharField(max_length=15)
    
class Fees(models.Model):
    Fee_id=models.CharField(max_length=10) 
    Amount=models.PositiveIntegerField()
    Balance=models.PositiveIntegerField()
    Status=models.CharField(max_length=40)
    Course=models.ForeignKey('Course', on_delete=models.CASCADE,related_name='Fees_Course') 

class Payment(models.Model):
    Payment_id=models.CharField(max_length=10)
    Student_roll_number=models.ForeignKey('Student',on_delete=models.CASCADE,related_name='Student_Payment')
    Amount=models.ForeignKey('Fees',on_delete=models.CASCADE,related_name='Course_Amount')
    Status=models.CharField(max_length=40)
    Payment_date=models.DateField()
    Due_date=models.DateTimeField()
    
          
      
      
    
        
    
