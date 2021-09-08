from typing import ChainMap
from django.db import models

import uuid
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    # MANT TO MANY RELATIONSHIP
    tags = models.ManyToManyField('Tag',blank=True)
    # tags = models.ManyToManyField(TAG_MODEL) > 'Tag' if the Tag model is not below this model > Tag if the Tag model is below this model

    # PROJECT VOTES
    # Calculate votes
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    # Calculate vote ratio
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


# CharField > Small field
    # max_length > sets the max length to the Field

# TextField > Larger Field
    # null=True > null is for database to know to accept empty field or not > True means allows empty field > False means doesnt
    # blank=True > blank is for django to know to accept empty field or not > True means allows empty field > False means doesnt

# DateTimeField > Date and Time Picker
    #auto_now_add > automatically creates date and time of model instance created

# UUIDField > 16 digit character
    #default=uuid.uuid4 > uuid4
    #unique > Means no other value in database can have this id
    #primary_key > use this as a primary_key or id
    # () as django creates an id by default , will be replaced by this id
    #editable > No one can edit this

# AFTER CREATING MODEL
#   WE HAVE TO PREPARE MIRATIONS AND MIGRATE > TO CREATE TABLES
#   AFTER PREPARING FOR MIGRATIONS > python manage.py makemigrations > WE CAN SEE A FOLDER migrations>0001_initial.py
#   THEN MIGRATE > python manage.py migrate > SO TABLES WILL BE CREATED IN DB

#   BUT WE CANNOT SEE THE TABLE IN ADMIN PANEL > 
#   WE NEED TO > REGISTER THE MODEL WITH ADMIN PANEL TO SEE > TABLE IN ADMIN PANEL
#   [APP FOLDER]>admin.py

# def __str__(self):
#         return self.title
# IS USED TO SHOW THE TITLE ON THE TABLE

# DATABASE RELATIONSHIPS
#       ONE TO ONE RELATIONSHIP
#       ONE TO MANY RELATIONSHIP > Eg: REVIEWS > PROJECTS TABLE (ID | TITLE | DESC) -- REVIEWS TABLE (ID | Parent_ID | BODY)
#       MANY TO MANY RELATIONSHIP > Eg: TAGS > PROJECTS TABLE (ID | TITLE | DESC) -- INTERMEDIARY TABLE(Proj_ID | Tag_ID ) -- TAGS TABLE(ID | TITLE | DESC)

# ONE TO MANY RELATIONSHIP MODEL
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    # owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

    #on_delete=models.SET_NULL > IF PROJECTS GET DELETED THEN REVIEW WILL BE NULL > project field will set to null
    #on_delete=models.CASCADE > IF PROJECTS GET DELETED THEN REVIEW WILL BE DELETED > delete all the reviews if project is deleted

    #models.ForeignKey(Project, on_delete=models.CASCADE) > LINKING THE PROJECT ID TO THIS REVIEWS CLASS 
    #   ForeignKey(CLASS_NAME_OF_MODEL_ID_REQUIRED, on_delete=WHAT_TO_BE_DONE)


# MANY TO MANY RELATIONSHIP MODEL
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


# DJANGO MODEL FORM
# Is a way to create a form based on a particular model
