import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from .constants import *


# Create your models here.
class MyAccountManager(BaseUserManager):

    def create_superuser(self, email):
        user = self.create_user(
            email=email,
        )
        user.is_active = True
        user.is_admin = True
        user.is_super_user = True
        user.is_staff = True

        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Sales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    last_login = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Sales'
        indexes = [
             models.Index(fields=[
                 'email'
             ])
        ]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['email']


class Developer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    developer_name = models.CharField(max_length=100, null=True, blank=True)
    company_id = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=200, null=True, blank=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, null=True, blank=True)
    year_of_experience = models.PositiveIntegerField(null=True, blank=True)
    induction_comment = models.TextField(null=True, blank=True)
    tech_stack = ArrayField(models.CharField(max_length=1000), null=True, blank=True)
    date_joined = models.DateField()
    is_engaged = models.BooleanField(default=False)

    class Meta:
        db_table = 'Developer'

    def __str__(self):
        return str(self.developer_name)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    project_name = models.CharField(max_length=100, null=True, blank=True)
    project_role = models.CharField(max_length=100, choices=ROLE_CHOICES, null=True, blank=True)
    project_tech_stack = ArrayField(models.CharField(max_length=1000), null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Project'


class Cilent(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    cilent_name = models.CharField(max_length=100, null=True, blank=True)
    cilent_company_name = models.CharField(max_length=100, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Cilent'


class Scheduled_Call(models.Model):
    cilent = models.ForeignKey(Cilent, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    meeting_link = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'Scheduled_call'




