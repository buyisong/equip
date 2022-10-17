# Generated by Django 3.2 on 2022-10-16 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp_picture', models.ImageField(upload_to='')),
                ('dp_urls', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsSpu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_name', models.CharField(max_length=32)),
                ('sp_details', models.CharField(max_length=256)),
                ('sp_picture', models.ImageField(upload_to='')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_goods.goodstype')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsSku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sk_name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
                ('price', models.CharField(max_length=32)),
                ('sale_volume', models.CharField(max_length=32)),
                ('axios', models.CharField(max_length=32)),
                ('connection', models.CharField(max_length=32)),
                ('refresh', models.CharField(max_length=32)),
                ('size', models.CharField(max_length=32)),
                ('rest', models.IntegerField()),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_goods.goodsspu')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_picture', models.ImageField(upload_to='')),
                ('sku_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_goods.goodssku')),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_picture', models.CharField(max_length=64)),
                ('index', models.CharField(db_index=True, max_length=32)),
                ('sku_carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_goods.goodssku')),
            ],
        ),
    ]
