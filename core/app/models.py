from django.db import models

# Create your models here.
class Post(models.Model):
    Status_Choices=(('active','Active'),('inactive','Inactive'),)
    site = models.CharField(max_length = 10, default=None)
    contact = models.CharField(max_length=20,default=None)
    capacity = models.IntegerField()
    location = models.CharField(max_length=20, default=None)
    mapped = models.IntegerField()
    status = models.CharField(max_length=9,choices=Status_Choices,default='active')
    description = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.site

class PostOBD(models.Model):
    status_choices=(('active','Active'),('inactive','Inactive'),)
    mapped_choices=(('assigned','Assigned'),('not assigned','Not Assigned'))
    model_choices = (('tag model 001', 'Tag Model 001'), ('tag model 002', 'Tag Model 002'))
    asset_choices=(('i20,hyundai', 'i20,Hyundai'), ('swift,maruthi', 'Swift,Maruthi'))
    tag_model= models.CharField(max_length=20, choices=model_choices, default='tag model 001')
    tag_name = models.CharField(max_length = 10, default=None)
    tag_mapped = models.CharField(max_length=20, choices=mapped_choices, default='assigned')
    car_asset= models.CharField(max_length=20, choices=asset_choices, default='i20,hyundai')
    site = models.CharField(max_length=20, default=None)
    location = models.CharField(max_length=20, default=None)
    status = models.CharField(max_length=9,choices=status_choices,default='active')
    description = models.CharField(max_length=200, default=None)
    def __str__(self):
        return self.tag_model

class PostCar(models.Model):
    mapped_choices=(('yes','Yes'),('no','No'),)
    demo_choices = (('yes', 'Yes'), ('no', 'No'),)
    status_choices = (('active', 'Active'), ('inactive', 'Inactive'),)
    model_choices = (('tag model 001', 'Tag Model 001'), ('tag model 002', 'Tag Model 002'),)
    alert_choices = (('online', 'Online'), ('offiline', 'Offline'),)
    car_model= models.CharField(max_length=20, default=None)
    car_brand = models.CharField(max_length = 10, default=None)
    site = models.CharField(max_length=20, default=None)
    location = models.CharField(max_length=20, default=None)
    tag_mapped = models.CharField(max_length=20, choices=mapped_choices, default='yes')
    status = models.CharField(max_length=9, choices=status_choices, default='active')
    tag_model = models.CharField(max_length=20, choices=model_choices, default='tag model 001')
    demo_model = models.CharField(max_length=9, choices=demo_choices, default='yes')
    alerts_time = models.CharField(max_length=9, choices=demo_choices, default='online')
    description = models.CharField(max_length=200, default=None)
    def __str__(self):
        return self.car_model
