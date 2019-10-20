# Generated by Django 2.2.6 on 2019-10-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('longt', models.FloatField()),
                ('langt', models.FloatField()),
                ('call', models.CharField(max_length=100)),
                ('emer_call', models.CharField(blank=True, max_length=100, null=True)),
                ('is_emergen', models.BooleanField()),
                ('is_night', models.BooleanField()),
                ('duty1', models.BooleanField()),
                ('duty2', models.BooleanField()),
                ('duty3', models.BooleanField()),
                ('duty4', models.BooleanField()),
                ('duty5', models.BooleanField()),
                ('duty6', models.BooleanField()),
                ('duty7', models.BooleanField()),
                ('duty8', models.BooleanField()),
                ('duty1_open', models.TimeField(blank=True, null=True)),
                ('duty1_close', models.TimeField(blank=True, null=True)),
                ('duty2_open', models.TimeField(blank=True, null=True)),
                ('duty2_close', models.TimeField(blank=True, null=True)),
                ('duty3_open', models.TimeField(blank=True, null=True)),
                ('duty3_close', models.TimeField(blank=True, null=True)),
                ('duty4_open', models.TimeField(blank=True, null=True)),
                ('duty4_close', models.TimeField(blank=True, null=True)),
                ('duty5_open', models.TimeField(blank=True, null=True)),
                ('duty5_close', models.TimeField(blank=True, null=True)),
                ('duty6_open', models.TimeField(blank=True, null=True)),
                ('duty6_close', models.TimeField(blank=True, null=True)),
                ('duty7_open', models.TimeField(blank=True, null=True)),
                ('duty7_close', models.TimeField(blank=True, null=True)),
                ('duty8_open', models.TimeField(blank=True, null=True)),
                ('duty8_close', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
