# Generated by Django 4.0 on 2022-09-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_sales_full_name_alter_sales_sale_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='role',
            field=models.CharField(choices=[('Back-end', 'Back-end'), ('Full-stack', 'Full-stack'), ('Front-end', 'Front-end'), ('Dev-ops', 'Dev-ops')], max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_role',
            field=models.CharField(blank=True, choices=[('Back-end', 'Back-end'), ('Full-stack', 'Full-stack'), ('Front-end', 'Front-end'), ('Dev-ops', 'Dev-ops')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
