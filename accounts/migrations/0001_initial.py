# Generated by Django 4.0 on 2022-09-12 06:04

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cilent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cilent_name', models.CharField(max_length=100)),
                ('cilent_company_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Cilent',
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('developer_name', models.CharField(max_length=100)),
                ('company_id', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('role', models.CharField(choices=[('Front-end', 'Front-end'), ('Full-stack', 'Full-stack'), ('Dev-ops', 'Dev-ops'), ('Back-end', 'Back-end')], max_length=100)),
                ('year_of_experience', models.FloatField()),
                ('induction_comment', models.TextField()),
                ('tech_stack', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), size=None)),
                ('date_joined', models.DateField()),
                ('is_engaged', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Developer',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_name', models.CharField(blank=True, max_length=100, null=True)),
                ('project_role', models.CharField(blank=True, choices=[('Front-end', 'Front-end'), ('Full-stack', 'Full-stack'), ('Dev-ops', 'Dev-ops'), ('Back-end', 'Back-end')], max_length=100, null=True)),
                ('project_tech_stack', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, null=True, size=None)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Project',
            },
        ),
        migrations.CreateModel(
            name='Scheduled_Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('meeting_link', models.CharField(blank=True, max_length=500, null=True)),
                ('cilent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.cilent')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.developer')),
            ],
            options={
                'db_table': 'Scheduled_call',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('sale_password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'db_table': 'Sales',
            },
        ),
        migrations.AddField(
            model_name='cilent',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.project'),
        ),
        migrations.AddIndex(
            model_name='sales',
            index=models.Index(fields=['email'], name='Sales_email_ae7d81_idx'),
        ),
    ]
