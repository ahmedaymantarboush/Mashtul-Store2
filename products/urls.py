from django.urls import path
from .views import *

app_name="products"

urlpatterns = [
    path("" , index ,name="index" ),
    path("products/product<int:productId>" , productDetails ,name="productDetails" ),
    path("products/actionFromProduct<int:productId>" , action ,name="productAction"),
    path("accounts/cart" , cart ,name="cart" ),
    path("accounts/wishes" , wishes ,name="wishes" ),
    path("accounts/myProducts" , myProducts ,name="myProducts" ),
    path("products/addProduct" , addProduct ,name="addProduct" ),
    path("products/add" , add ,name="add"),

]