from django.shortcuts import render
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product , Product_Instance, Brand, Category
# Create your views here.



def email_check(user):
    return user.email.endswith('@example.com')
#@login_required
#user_passes_test(email_check)
def index(request):
    
    num_Product = Product.objects.all().count()
    num_instances = Product_Instance.objects.all().count()
    #num_instances_available = Product_instance.obj.filter()
    num_Brand = Brand.objects.all().count()
    
    context = {
        'num_Product' : num_Product,
        'num_instances' : num_instances,
        'num_Brand' : num_Brand,

    }
    return render(request, 'almasroyan/index.html', context)


class ProductListView(LoginRequiredMixin,generic.ListView):
    model = Product
    context_object_name = "product_list"
    template_name = 'almasroyan\product_list.html'
    #queryset = Product.objects.filter(name__icontains = 'hair')
    #def get_queryset(self):
    #   return Product.objects.filter(name__icontains = 'hair')
    paginate_by = 1

class ProductDetailView(generic.DetailView):
    model = Product
    queryset = Product.objects.all()

    def get_object(self):
        obj = super().get_object()

        return obj
    
    

def contact(request):

    context = {

    }

    return render(request, 'almasroyan/contact.html',context)

def test(request):

    context = {

    }

    return render(request, 'almasroyan/test.html',context)