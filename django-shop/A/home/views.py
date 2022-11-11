from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category
from . import tasks
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from utils import IsAdminUserMixin
from orders.forms import CartAddProductForm


class HomeView(View):
    def get(self, request, category_slug: str = None):
        products = Product.objects.filter(availabe=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home/home.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = CartAddProductForm()
        return render(request, 'home/detail.html', {'product': product, 'form': form})


# class BucketHomeView(UserPassesTestMixin, View):
class BucketHomeView(IsAdminUserMixin, View):
    template_name = 'home/bucket.html'

    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        # age async bod
        # objects = all_bucket_objects_task.delay()
        return render(request, self.template_name, {'objects': objects})

    # def test_func(self):
    #     return self.request.user.is_authenticated and self.request.user.is_admin


# class DeleteBucketObjView(UserPassesTestMixin, View):
class DeleteBucketObjView(IsAdminUserMixin, View):
    def get(self, request, key):
        # delay(key) ta selery ino async seda bezane
        tasks.delete_object_task.delay(key)
        messages.success(request, 'Object deleted successfully sooooon', 'info')
        return redirect('home:bucket')

    # def test_func(self):
    #     return self.request.user.is_authenticated and self.request.user.is_admin


# class DownloadBucketObjView(UserPassesTestMixin, View):
class DownloadBucketObjView(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.download_object_task.delay(key)
        messages.success(request, 'Object downloaded successfully sooooon', 'info')
        return redirect('home:bucket')

    # def test_func(self):
    #     return self.request.user.is_authenticated and self.request.user.is_admin
