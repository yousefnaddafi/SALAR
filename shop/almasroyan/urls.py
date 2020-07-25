from django.urls import path, re_path

from . import views


app_name = 'almasroyan'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('list',views.ProductListView.as_view(), name= 'ProductList'),
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name= 'ProductDetail'),
    path('contact', views.contact, name= 'contact'),
    path('test',views.test, name= 'test'),
]
 