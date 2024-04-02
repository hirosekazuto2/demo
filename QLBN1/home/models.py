from django.db import models

class Patient(models.Model):
    idP = models.CharField(primary_key=True, max_length=100)
    NameP = models.CharField(max_length=100)
    Dob = models.DateTimeField(verbose_name="Date of Birth", auto_now=True)
    # Assuming Sex field represents gender, let's rename it and provide choices
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender",default='M')
    Phone_Number = models.CharField(max_length=20, verbose_name="Phone Number")
    Address = models.CharField(max_length=1000)

    def __str__(self):
        return self.NameP
