from django.db import models

# Create your models here.
class Asset(models.Model):
    uid = models.ForeignKey('Register',on_delete=models.DO_NOTHING, null=True, db_column='uid')
    asset_id = models.AutoField(primary_key=True)
    driver = models.CharField(max_length=50)
    asset_duration = models.IntegerField()
    rent_amount = models.IntegerField()

    class Meta:
        db_table = 'asset'


class FarmerActivity(models.Model):
    uid = models.ForeignKey('Register',on_delete=models.DO_NOTHING, null=True, db_column='uid')
    activity_name = models.CharField(max_length=50)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    activity_proof = models.TextField()

    class Meta:
        db_table = 'farmer_activity'


class FarmerDetails(models.Model):
    uid = models.ForeignKey('Register', on_delete=models.DO_NOTHING, null=True,db_column='uid')
    loc_lat = models.CharField(max_length=50)
    loc_long = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    land_size = models.FloatField()
    number_seedling = models.IntegerField()

    class Meta:
        db_table = 'farmer_details'


class MaterialsConsumed(models.Model):
    uid = models.ForeignKey('Register', on_delete=models.DO_NOTHING, null=False, db_column='uid')
    material = models.CharField(max_length=50)
    amount = models.IntegerField()
    bill = models.CharField(max_length=150, db_collation='latin1_swedish_ci')

    class Meta:
        db_table = 'materials_consumed'


class PeopleInvolved(models.Model):
    amount_payable = models.IntegerField()
    uid = models.ForeignKey('Register', on_delete=models.DO_NOTHING, null=False, db_column='uid')
    worker_name = models.CharField(max_length=50)
    duration = models.IntegerField()
    amount_paid = models.IntegerField()

    class Meta:
        db_table = 'people_involved'


class Production(models.Model):
    uid = models.ForeignKey('Register',on_delete=models.DO_NOTHING, null=False, db_column='uid')
    type_material = models.CharField(max_length=50)
    units = models.IntegerField()
    storage_location = models.CharField(max_length=150)
    class Meta:
        db_table = 'production'


class Register(models.Model):
    uid = models.AutoField(primary_key=True)
    phone = models.BigIntegerField(unique=True)
    password = models.TextField(max_length=50)
    type = models.IntegerField(default=0)

    def __int__(self):
        return self.uid
    
    class Meta:
        db_table = 'register'