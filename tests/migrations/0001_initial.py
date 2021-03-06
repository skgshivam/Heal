# Generated by Django 3.0.5 on 2020-07-24 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lab1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='media_/physio_profile_pic/')),
                ('name', models.CharField(default='', max_length=100)),
                ('condition', models.CharField(choices=[('ALLERGY', 'ALLERGY'), ('ANEMIA', 'AMENIA')], default='', max_length=100)),
                ('test_type', models.CharField(choices=[('BLOOD', 'BLOOD'), ('URINE', 'URINE')], default='', max_length=100)),
                ('price', models.FloatField(default=0)),
                ('discounted_price', models.FloatField(default=0)),
                ('pre_test_information', models.CharField(default='', max_length=256)),
                ('description', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TestLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab1.Lab1')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Test')),
            ],
        ),
    ]
