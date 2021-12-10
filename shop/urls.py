from django.urls import path, include
from . import views

urlpatterns=[
	path('',views.main),
	path('all',views.index, name='all'),
	path('product_list',views.product_list,name="product_list"),
	path('shop_list',views.shop_list, name="shop_list"),
	path('deal_list',views.deal_list,name='deal_list')
]


