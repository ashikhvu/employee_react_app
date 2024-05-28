from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cource_completed = models.CharField(max_length=255)
    date = models.DateTimeField(auto_add_now=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255,unique=True)
    address = models.TextField()
    document = models.FileField(upload_to='media/',blank=True,null=True)
    
    def __str__(self):
        return self.first_name
    
class TeamLeadModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255,unique=True)
    address = models.TextField()

class ProjectModel(models.model):
    employee= models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,null=True,blank=True)
    team_lead= models.ForeignKey(TeamLeadModel,on_delete=models.CASCADE,null=True,blank=True)
    project_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    submission_date = models.DateTimeField()
    docuemnt = models.FileField()
    status=models.CharField(max_length=255)
    notes=models.TextField()

