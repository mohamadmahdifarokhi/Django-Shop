# Generated by Django 4.0.3 on 2022-10-30 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام دسته بندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ دسته بندی')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ محصول')),
                ('image', models.ImageField(upload_to='products/', verbose_name='تصویر محصول')),
                ('description', models.TextField(verbose_name='توضیحات محصول')),
                ('price', models.IntegerField(verbose_name='قیمت محصول')),
                ('availabe', models.BooleanField(default=True, verbose_name='موجودی')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='home.category', verbose_name='دسته بندی')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
