from django.db import models





class department(models.Model):
    department=models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    def __str__(self):
        return self.department

class Doctortable(models.Model):
    doctortable=models.CharField(max_length=200)
    docspec=models.CharField(max_length=500)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    doctimage=models.ImageField(upload_to="main")
    def __str__(self):
        return self.doctortable

class Detailstable(models.Model):
        doctdetails=models.CharField(max_length=200)
        doctdescription=models.TextField(max_length=500)
        doctimage=models.ForeignKey(Doctortable,on_delete=models.CASCADE)

# Create your models here.
