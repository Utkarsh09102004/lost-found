# Generated by Django 4.2.7 on 2023-11-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='founditem',
            name='contact_info',
        ),
        migrations.RemoveField(
            model_name='lostitem',
            name='contact_info',
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='date_lost',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]