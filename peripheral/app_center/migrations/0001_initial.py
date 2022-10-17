# Generated by Django 3.2 on 2022-10-16 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=64)),
                ('a_status', models.IntegerField()),
                ('a_phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('og_count', models.IntegerField()),
                ('og_price', models.IntegerField()),
                ('og_talk', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='OrderMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('count', models.IntegerField()),
                ('pay_status', models.IntegerField(default=0)),
                ('c_time', models.DateField()),
                ('address_order_mes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_center.address')),
            ],
        ),
    ]
