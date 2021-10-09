from django import forms
from .models import ProgressModel

class ProgressForm(forms.ModelForm):
    # CITIES_AVAILABLE = (
    #     ('Pr','Peshawar'),
    #     ('Lr','Lahore'),
    #     ('Isl','Islamabad')
    # )
    # city = forms.ChoiceField (choices = CITIES_AVAILABLE,widget = forms.Select(),required = True)
    
    VARIETY = (
        ('Inv','Invoice'),
        ('Quo','Quotation'),
        ('Rep','Report')
    )
    typ = forms.ChoiceField ( choices = VARIETY,widget = forms.RadioSelect(),required = True)


    # added_at = forms.DateTimeField()
    # added_by = forms.CharField()  

    ######### DEPENDS ONLY ON Type ##########
    ########## REPORT #############
    # ProjectID = forms.CharField(required = False)  
    # Location = forms.CharField(required = False)  
    # ProjectName = forms.CharField(required = False)  
    # NoOfBH = forms.CharField(required = False)  
    # DepthOfBH = forms.CharField(required = False)  
    # Drilling_Method = forms.CharField(required = False)  
    # DateOfDrilling = forms.DateTimeField (required = False)
    # ReportingOfficer = forms.CharField(required = False)  
    # SubmittedTo = forms.CharField(required = False)  
    # GroundWaterTableDepth = forms.CharField(required = False)  
    
    # ############# Invoice ############ 
    # #### DATE WILL BE INCLUDED LATER ON #### INCLUDED ONLY WITH Consultancy and Operations Start and End
    # InvoiceTypeAvailable =  (
    #     ('F&D','Feasibility & Designs'),
    #     ('Cons','Consultancy'),
    #     ('Op','Operation')
    # )
    # InvoiceTypes = forms.ChoiceField ( choices = InvoiceTypeAvailable,required = False)
    # InvAmount = forms.CharField(required = False) 

    # ################ QUOTATION ##################
    # QuotAmount = forms.CharField(required = False)  
    # QuotClientName = forms.CharField(required = False)
    



    class Meta:
        model = ProgressModel
        fields = "__all__"
    # widget = {
    #         "ProjectID" : forms.CharField(),
    #         "Location" : forms.CharField(),
    #         "ProjectName" : forms.CharField(), 
    #         "NoOfBH" : forms.CharField(),
    #         "DepthOfBH" : forms.CharField(),
    #         "Drilling_Method" : forms.CharField(),
    #         "DateOfDrilling" : forms.DateTimeField (),
    #         "ReportingOfficer" : forms.CharField(),
    #         "SubmittedTo" : forms.CharField(),
    #         "GroundWaterTableDepth" : forms.CharField(),
    
    # }

    