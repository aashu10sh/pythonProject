from django.urls import path, include
from . import views

urlpatterns=[
	path('',views.main),
	# path('all',views.index, name='all'),
	# path('product_list',views.product_list,name="product_list"),
	# path('shop_list',views.shop_list, name="shop_list"),
	# path('deal_list',views.deal_list,name='deal_list'),
	# path('product_form',views.product_form,name="product_form"),
	# path('product_data',views.product_data,name="product_data"),
	# path('product/<int:id>/<str:name>', views.product, name="product"),
	# path('user', views.user, name='usera'),
	path("product",views.product, name='product'),
	path("productshow",views.productshow,name="productshow"),
	path("productedit/<int:id>",views.productedit,name="productedit"),
	path("productupdate/<int:id>",views.productupdate,name="productupdate"),
	path("productdestroy/<int:id>", views.productdestroy, name="productdestroy")



]


