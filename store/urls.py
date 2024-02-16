from django.urls import path,include
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('',index),
    path('category/<int:category_id>', CategoryById.as_view(), name='get_product_by_category'),
    path('SignUp',SignUp.as_view() , name='signup'),
    # url(r'^home/category/(?P<category_id>.+)$', CategoryById.as_view() ,name='get_product_by_category'),
]