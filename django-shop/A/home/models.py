from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ دسته بندی')

    class Meta:
        ordering = ['name']
        verbose_name = 'my_category'
        # bara dastan s jam
        verbose_name_plural = 'my_categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_filter', args=[self.slug])


class Product(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته بندی')
    category = models.ManyToManyField(Category, related_name='products', verbose_name='دسته بندی')
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ محصول')
    # image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='تصویر محصول')
    image = models.ImageField(verbose_name='تصویر محصول')
    # description = models.TextField(verbose_name='توضیحات محصول')
    description = RichTextField(verbose_name='توضیحات محصول')
    # decimal_places=2 means that we have 2 digits after the decimal point
    # max_digits=10 means that we have 10 digits in total
    # example: 123456789.12
    # price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    availabe = models.BooleanField(default=True, verbose_name='موجودی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_detail', args=[self.slug])
