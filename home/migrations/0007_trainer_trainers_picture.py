# Generated by Django 4.1 on 2022-08-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_schedule_schedule_id_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='Trainers_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
