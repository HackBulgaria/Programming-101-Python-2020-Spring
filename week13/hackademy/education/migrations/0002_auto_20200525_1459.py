# Generated by Django 3.0.6 on 2020-05-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
