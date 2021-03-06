# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asset(models.Model):
    uid = models.ForeignKey('Register', models.DO_NOTHING, db_column='uid')
    asset_id = models.AutoField(primary_key=True)
    driver = models.CharField(max_length=50)
    asset_duration = models.IntegerField()
    rent_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'asset'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FarmerActivity(models.Model):
    uid = models.ForeignKey('Register', models.DO_NOTHING, db_column='uid')
    activity_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    activity_proof = models.TextField()

    class Meta:
        managed = False
        db_table = 'farmer_activity'


class FarmerDetails(models.Model):
    uid = models.ForeignKey('Register', models.DO_NOTHING, db_column='uid')
    loc_lat = models.CharField(max_length=50)
    loc_long = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    land_size = models.IntegerField()
    number_seedling = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'farmer_details'


class MaterialsConsumed(models.Model):
    uid = models.ForeignKey('Register', models.DO_NOTHING, db_column='uid')
    material = models.CharField(max_length=50)
    amount = models.IntegerField()
    bill = models.CharField(max_length=150, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'materials_consumed'


class PeopleInvolved(models.Model):
    amount_payable = models.IntegerField()
    uid = models.ForeignKey('Register', models.DO_NOTHING, db_column='uid')
    worker_name = models.CharField(max_length=50)
    duration = models.IntegerField()
    amount_paid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'people_involved'


class Production(models.Model):
    uid = models.ForeignKey('Register', models.DO_NOTHING, db_column='uid')
    type_material = models.CharField(max_length=50)
    units = models.IntegerField()
    storage_location = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'production'


class Register(models.Model):
    uid = models.AutoField(primary_key=True)
    phone = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=50)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'register'
