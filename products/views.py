from django.shortcuts import get_object_or_404,render

from .models import Category, Product

# Create your views here.
def product_list_view(request):
    products = Product.objects.all()[:30]
    context = {"products": products}
    return render(
        template_name='products/product-list.html',
        context=context,
        request=request,
    )


def product_single_view(request, product_id):
    p = get_object_or_404(Product,id=product_id)
    context = {"product": p}
    return render(
                template_name='products/product-single.html',
                context=context,
                request=request,
    )
