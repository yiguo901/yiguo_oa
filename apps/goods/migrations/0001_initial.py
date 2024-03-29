# Generated by Django 2.0.1 on 2019-07-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='一级分类')),
                ('category_id', models.IntegerField(verbose_name='分类id')),
            ],
            options={
                'verbose_name': '一级分类',
                'verbose_name_plural': '一级分类',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=50, verbose_name='二级分类')),
                ('child_id', models.IntegerField(verbose_name='分类id')),
                ('category_id', models.IntegerField(verbose_name='一级分类id')),
                ('child_img', models.CharField(max_length=200, verbose_name='类图片')),
            ],
            options={
                'verbose_name': '二级分类',
                'verbose_name_plural': '二级分类',
                'db_table': 'child',
            },
        ),
        migrations.CreateModel(
            name='YGGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='商品分类')),
                ('child_name', models.CharField(max_length=50, verbose_name='分类详情')),
                ('name', models.CharField(max_length=50, verbose_name='商品名称')),
                ('detail_name', models.CharField(max_length=100, null=True, verbose_name='商品描述')),
                ('price', models.FloatField(verbose_name='商品价格')),
                ('marketprice', models.FloatField(verbose_name='市场价格')),
                ('goods_wheel_img', models.CharField(max_length=5000, null=True, verbose_name='轮播图')),
                ('pro_addr', models.CharField(max_length=200, verbose_name='生产地')),
                ('detail_img_url', models.CharField(max_length=5000, verbose_name='详情页图片')),
                ('sale', models.IntegerField(verbose_name='销量')),
                ('stock', models.IntegerField(verbose_name='库存')),
                ('category_id', models.IntegerField(verbose_name='详情id')),
                ('child_id', models.IntegerField(verbose_name='分类id')),
                ('goods_img', models.CharField(max_length=500, verbose_name='商品图片')),
                ('is_chosen', models.BooleanField(default=False, verbose_name='是否精选')),
            ],
            options={
                'verbose_name': '商品表',
                'verbose_name_plural': '商品表',
                'db_table': 'goods',
            },
        ),
    ]
