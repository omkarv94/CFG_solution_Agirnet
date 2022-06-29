from atexit import register
from django.shortcuts import render, HttpResponse
from home.models import Register,Production,PeopleInvolved,MaterialsConsumed,FarmerDetails,FarmerActivity,Asset 
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

def contact(request):
    return render(request,"contact.html")
    
def homepage(request):
    return render(request,"homepage.html")


import os    
def analytics(request):
    
    os.system('cmd /c "C:\\Program Files\\Tableau\\Tableau 2022.1\\bin\\tableau.exe"')
    return render(request, "pd.html")

def about(request):
    return render(request, "about.html")

def dash(request):
    return render(request,"dash.html")

# Create your views here.
def index(request):
    return render(request, 'index.html')



# add user/admin - 0/1
def registration(request):
    if request.method=='POST':
        insert=Register()
        insert.phone=request.POST.get('phone')
        insert.password=request.POST.get('fpass')
        if request.POST.get('type')=="1":
            insert.type=request.POST.get('type')
            
        insert.save()
        return HttpResponseRedirect(reverse(login))

    return render(request, 'registration.html')
#PLEASE DO NOT EDIT IN LOGIN AND REGISTER (alekhya :) )

def login(request):

    if request.method=='POST':
        
        phone=request.POST.get('phone')
        pasword=request.POST.get('password')
        
        
        login=Register.objects.filter(phone=phone, password=pasword).values()
        if login:
            return HttpResponseRedirect(reverse(form,args=(phone,)))
        else:
            messages.error(request, 'Incorrect Credentials')
            
    return render(request,"login.html")




def pd(request):
    return render(request,"pd.html")


def activityreplit(request):
    if request.method == 'POST':
        
        insert_form = FarmerActivity()            #1
        register = Register.objects.get(uid=1)
  
        activity_name = request.POST.get('activity_name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        activity_proof = request.POST.get('activity_proof')        
        insert_form.activity_name=request.POST.get('activity_name')
        insert_form.start_date=str(request.POST.get('start_date'))
        insert_form.end_date=str(request.POST.get('end_date'))
        insert_form.uid = register
        insert_form.activity_proof=request.POST.get('activity_proof')
        insert_form.save()
        
        
        insert_detail = PeopleInvolved()        #2
        amount_payable = request.POST.get('amount_payable')
        worker_name = request.POST.get('worker_name')
        duration = request.POST.get('duration')
        amount_paid = request.POST.get('amount_paid')
        insert_detail.amount_payable=request.POST.get('amount_payable')
        insert_detail.worker_name=request.POST.get('worker_name')
        insert_detail.duration=request.POST.get('duration')
        insert_detail.amount_paid=request.POST.get('amount_paid')
        insert_detail.uid = register
        insert_detail.save()


        insert_asset = Asset()        #3
        driver = request.POST.get('driver')
        asset_duration = request.POST.get('asset_duration')
        rent_amount = request.POST.get('rent_amount')
        
        insert_asset.driver=request.POST.get('driver')
        insert_asset.asset_duration=request.POST.get('asset_duration')
        insert_asset.rent_amount =request.POST.get('rent_amount')
        insert_asset.uid = register
        insert_asset.save()


        insert_material= MaterialsConsumed()       #4
        material = request.POST.get('material')
        amount = request.POST.get('amount')
        bill = request.POST.get('bill')
        insert_material.material=request.POST.get('material')
        insert_material.amount=request.POST.get('amount')
        insert_material.bill=request.POST.get('bill')
        insert_material.uid = register
        insert_material.save()



        insert_production= Production()       #5
        type_material = request.POST.get('type_material')
        units = request.POST.get('units')
        storage_location = request.POST.get('storage_location')
        
        insert_production.type_material=request.POST.get('type_material')
        insert_production.units=request.POST.get('units')
        insert_production.storage_location=request.POST.get('storage_location')
        insert_production.uid = register
        insert_production.save()  

        
        insert_details= FarmerDetails()         #6 
        loc_lat = request.POST.get('loc_lat')
        loc_long = request.POST.get('loc_long')
        address = request.POST.get('address')
        land_size = request.POST.get('land_size')
        number_seedling = request.POST.get('number_seedling')

        insert_details.loc_lat=request.POST.get('loc_lat')
        insert_details.loc_long=request.POST.get('loc_long')
        insert_details.address=request.POST.get('address')
        insert_details.land_size=request.POST.get('land_size')
        insert_details.number_seedling=request.POST.get('number_seedling')
        insert_details.uid = register
        insert_details.save()

        return HttpResponseRedirect(reverse(homepage))

    else:
        return render(request,"activityreplit.html")


def form(request,pk):
    uid = pk
    register = Register.objects.get(phone=pk)
    
    if request.method == 'POST':
        
        insert_form = FarmerActivity()                  #1
                  
        insert_form.uid = register
        insert_form.activity_name=request.POST.get('activity_name')
        insert_form.start_date=request.POST.get('start_date')
        insert_form.end_date=request.POST.get('end_date')
        insert_form.activity_proof=request.POST.get('activity_proof')
        
        insert_form.save()
        
        insert_form2 = PeopleInvolved()                 #2

        insert_form2.uid = register
        insert_form2.amount_payable=request.POST.get('amount_payable')
        insert_form2.worker_name=request.POST.get('worker_name')
        insert_form2.duration=request.POST.get('duration')
        insert_form2.amount_paid=request.POST.get('amount_paid')
        
        insert_form2.save()
            
        insert_form3 = Asset()                          #3

        insert_form3.uid = register
        insert_form3.asset_id=request.POST.get('asset_id')
        insert_form3.driver=request.POST.get('driver')
        insert_form3.asset_duration=request.POST.get('asset_duration')
        insert_form3.rent_amount=request.POST.get('rent_amount')
        
        insert_form3.save()
            
        
        
        insert_form4 = MaterialsConsumed()                          #4

        insert_form4.uid = register
        insert_form4.material=request.POST.get('material')
        insert_form4.amount=request.POST.get('amount')
        insert_form4.bill=request.POST.get('bill')
        insert_form4.save()

        insert_form5 = Production()         #5

        insert_form5.uid = register
        insert_form5.type_material=request.POST.get('type_material')
        insert_form5.units=request.POST.get('units')
        insert_form5.storage_location=request.POST.get('storage_location')
        insert_form5.save()
        
        
        insert_form6 = FarmerDetails()     #6

        insert_form6.uid = register
        insert_form6.loc_lat=request.POST.get('loc_lat')
        insert_form6.loc_long=request.POST.get('loc_long')
        insert_form6.address=request.POST.get('address')
        insert_form6.land_size=request.POST.get('land_size')
        
        insert_form6.number_seedling=request.POST.get('number_seedling')
        insert_form6.save()
        
   
        
        """insert_production= Production()       #5
        type_material = request.POST.get('type_material')
        units = request.POST.get('units')
        storage_location = request.POST.get('storage_location')
        insert_production.type_material=request.POST.get('type_material')
        insert_production.units=request.POST.get('units')
        insert_production.storage_location=request.POST.get('storage_location')
        insert_production.uid = register
        insert_production.save()  

        
        insert_details= FarmerDetails()         #6 
        loc_lat = request.POST.get('loc_lat')
        loc_long = request.POST.get('loc_long')
        address = request.POST.get('address')
        land_size = request.POST.get('land_size')
        number_seedling = request.POST.get('number_seedling')

        insert_details.loc_lat=request.POST.get('loc_lat')
        insert_details.loc_long=request.POST.get('loc_long')
        insert_details.address=request.POST.get('address')
        insert_details.land_size=request.POST.get('land_size')
        insert_details.number_seedling=request.POST.get('number_seedling')
        insert_details.uid = register
        insert_details.save()
        
        """
        
        
        return HttpResponseRedirect(reverse(homepage))

    else:
        return render(request,"activityreplit.html")

