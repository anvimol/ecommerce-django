from django.shortcuts import render


# Create your views here.
def cart(request, total=0, quantity=0, cart_items=None):
    # try:
    #     cart = Cart.objects.get(cart_id=_cart_id(request))
    #     cart_items = cart_item = CartItem.objects.filter(cart=cart, is_active=True)
    #     for cart_item in cart_items:
    #         total += (cart_item.product.price * cart_item.quantity)
    #         quantity += cart_item.quantity
    #     tax = (2*total) / 100
    #     grand_total = total + tax
    # except ObjectDoesNotExist:
    #     pass
    #
    # context = {
    #     'total': total,
    #     'quantity': quantity,
    #     'cart_items': cart_items,
    #     'tax': tax,
    #     'grand_total': grand_total
    # }

    return render(request, 'store/cart.html')
