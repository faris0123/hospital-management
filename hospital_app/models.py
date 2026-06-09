from django.db import models

# Create your models here.
class Department(models.Model):
    dp_name = models.CharField(max_length=100)
    dp_description = models.TextField()

    def __str__(self):
        return self.dp_name
    
class Doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=150)
    dp_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='profile_pic')

    def __str__(self):
        return self.doc_name
    
class Booking(models.Model):
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=15)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date = models.DateField()

    def __str__(self):
        return self.p_name