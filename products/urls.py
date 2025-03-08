from django.urls import path
from .views import product_single_view,product_list_view



urlpatterns = [
    path('', product_list_view),
    path('<int:product_id>/', product_single_view),

]