import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from .constants import *
from django.dispatch import receiver
from django.db.models.signals import post_save


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


class Sales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200)
    last_login = models.DateField(auto_now=True)
    sale_password = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'Sales'
        indexes = [
             models.Index(fields=[
                 'email'
             ])
        ]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return str(self.full_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Sales.objects.create(user=instance, email=instance.username)


class Developer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    developer_name = models.CharField(max_length=100)
    company_id = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=200)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    year_of_experience = models.FloatField()
    induction_comment = models.TextField()
    tech_stack = ArrayField(models.CharField(max_length=1000))
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

    def __str__(self):
        return str(self.project_name)


class Cilent(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    cilent_name = models.CharField(max_length=100)
    cilent_company_name = models.CharField(max_length=100)
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

class project_client_dev(models.Model):
    dev_uuid = models.CharField(max_length=100)
    client_uuid = models.CharField(max_length=100)
    project_uuid = models.CharField(max_length=100)



