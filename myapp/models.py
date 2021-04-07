from django.db import models

state = (('delhi','Delhi'),('mumbai','Mumbai'))

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length = 100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=state,max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(blank = False,upload_to ='profileimg')
    my_file = models.FileField(blank=False,upload_to='doc')

