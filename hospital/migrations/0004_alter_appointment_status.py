# Generated by Django 5.0.3 on 2024-03-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Complete')], default='P', max_length=1),
        ),
    ]