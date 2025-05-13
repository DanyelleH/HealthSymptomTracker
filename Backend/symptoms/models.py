from django.db import models
from django.utils import timezone
# Create your models here.
class SeverityChoices(models.TextChoices):
    SEVERE = 'SEVERE',"Severe"
    MILD = "MILD","Mild"
    MODERATE = "MODERATE","Moderate"

from django.db import models

class SymptomLocation(models.TextChoices):
    HEAD = 'head', 'Head'
    NECK = 'neck', 'Neck'
    CHEST = 'chest', 'Chest'
    ABDOMEN = 'abdomen', 'Abdomen'
    BACK = 'back', 'Back'
    LEFT_ARM = 'left_arm', 'Left_Arm'
    LEFT_LEG = 'left_leg', 'Left_Leg'
    RIGHT_ARM = 'right_arm', 'Right_Arm'
    RIGHT_LEG = 'right_leg', 'Right_Leg'
    PELVIS = 'pelvis', 'Pelvis'
    WHOLE_BODY = 'whole_body', 'Whole Body'
    OTHER = 'other', 'Other'

class Symptoms(models.Model):
    name = models.CharField(max_length = 50)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    severity = models.CharField(max_length=15, choices=SeverityChoices.choices, default="MILD")
    location = models.CharField(max_length=20, choices=SymptomLocation.choices, default=SymptomLocation.OTHER)
    triggers = models.CharField(blank=True)
    relief = models.CharField(blank=True)
    notes= models.CharField(blank=True)
    
    def duration(self):
        """
        Get the length of time a symptom has been occuring
        """
        end = self.end_time or timezone.now
        return end - self.start_time