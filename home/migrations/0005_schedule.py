# Generated by Django 4.1 on 2022-08-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_course_course_id_alter_course_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Schedule_id', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
