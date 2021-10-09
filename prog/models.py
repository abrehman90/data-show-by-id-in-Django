from django.db import models
from django.utils import timezone

# Create your models here.
class ProgressModel (models.Model):

    ############# MAIN MENU #############
    #### DONT FORGET SERIAL NUMBER ####
    CITIES_AVAILABLE = (
        ('Pr','Peshawar'),
        ('Lr','Lahore'),
        ('Isl','Islamabad')
    )
    city = models.CharField (max_length = 3, choices = CITIES_AVAILABLE, default = 'Pr')
    
    VARIETY = (
        ('Inv','Invoice'),
        ('Quo','Quotation'),
        ('Rep','Report')
    )
    typ = models.CharField (max_length = 3, choices = VARIETY, default = 'Inv')

    added_at = models.DateTimeField(auto_now_add=True,)
    # added_by = models.CharField(blank=True,max_length=50)  

    ######### DEPENDS ONLY ON Type ##########
    ########## REPORT #############
    ProjectID = models.CharField(blank=True,max_length=12)  
    Location = models.CharField(blank=True,max_length=100)  
    ProjectName = models.CharField(blank=True,max_length=50)  
    NoOfBH = models.CharField(blank=True,max_length=10)  
    DepthOfBH = models.CharField(blank=True,max_length=20)  
    Drilling_Method = models.CharField(blank=True,max_length=50)  
    DateOfDrilling = models.DateTimeField (blank=True,auto_now = True)
    ReportingOfficer = models.CharField(blank=True,max_length=50)  
    SubmittedTo = models.CharField(blank=True,max_length=50)  
    GroundWaterTableDepth = models.CharField(blank=True,max_length=50)  
    
    ############# Invoice ############ 
    #### DATE WILL BE INCLUDED LATER ON #### INCLUDED ONLY WITH Consultancy and Operations Start and End
    InvoiceTypeAvailable =  (
        ('F&D','Feasibility & Designs'),
        ('Cons','Consultancy'),
        ('Op','Operation')
    )
    InvoiceTypes = models.CharField (blank=True,max_length = 5, choices = InvoiceTypeAvailable, default = 'Cons')
    InvAmount = models.CharField(blank=True,max_length=50) 

    ################ QUOTATION ##################
    QuotAmount = models.CharField(blank=True,max_length=50)  
    QuotClientName = models.CharField(blank=True,max_length=50)
    ### DATE WILL BE INCLUDED ON DEMAND ####

    def __str__ (self):
        return self.typ