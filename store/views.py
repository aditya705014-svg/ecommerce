from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required(login_url='/accounts/login/')
def store(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {'products': products})

@login_required(login_url='/accounts/login/')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})
def profile(request):
    return render(request, "store/profile.html")   


# store/views.py
from django.shortcuts import render, redirect
from django.http import Http404

# 🔹 TEMP data (ids: 1..6). Image paths static/ ke andar ke hi rakh lo.
PRODUCTS = {
    1: {
        "name": "Apple iPhone 11 (Black, 64GB)",
        "price": 39999,
        "description": "A13 Bionic, dual camera.",
        "image_static": "images/11.avif",
    },
    2: {
        "name": "Apple iPhone 12 Pro (Gold, 64GB)",
        "price": 69999,
        "description": "A14 Bionic, triple camera.",
        "image_static": "images/12pro.webp",
    },
    3: {
        "name": "Apple iPhone 13 (Yellow, 64GB)",
        "price": 54999,
        "description": "A15 Bionic, superb battery.",
        "image_static": "images/13.jpg",
    },
    4: {
        "name": "Apple iPhone 13 Pro (Blue, 64GB)",
        "price": 79999,
        "description": "ProMotion OLED, triple cam.",
        "image_static": "images/13pro.jpg",
    },
    5: {
        "name": "Apple iPhone 13 Pro Max (Blue, 512GB)",
        "price": 99999,
        "description": "Big battery, big display.",
        "image_static": "images/13promax.jpg",  # agar alag file hai to update
    },
    6: {
        "name": "Apple iPhone 14 (Blue, 128GB)",
        "price": 69999,
        "description": "Crash detection, great perf.",
        "image_static": "images/14r.webp",
    },
}

def store(request):
    # aapka existing list page render hota rahe
    return render(request, "store/store.html")

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order

# Product detail page (Buy button ke baad yahi chalega)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/checkout.html", {"product": product, "pk": pk})


from django.shortcuts import render, redirect
from django.http import Http404

# Ye aapka TEMP data hai
PRODUCTS = {
    1: {
        "name": "Apple iPhone 11 (Black, 64GB)",
        "price": 39999,
        "description": "A13 Bionic, dual camera.",
        "image_static": "images/11.avif",
    },
    2: {
        "name": "Apple iPhone 12 Pro (Gold, 64GB)",
        "price": 69999,
        "description": "A14 Bionic, triple camera.",
        "image_static": "images/12pro.webp",
    },
    3: {
        "name": "Apple iPhone 13 (Yellow, 64GB)",
        "price": 54999,
        "description": "A15 Bionic, superb battery.",
        "image_static": "images/13.jpg",
    },
    4: {
        "name": "Apple iPhone 13 Pro (Blue, 64GB)",
        "price": 79999,
        "description": "ProMotion OLED, triple cam.",
        "image_static": "images/13pro.jpg",
    },
    5: {
        "name": "Apple iPhone 13 Pro Max (Blue, 512GB)",
        "price": 99999,
        "description": "Big battery, big display.",
        "image_static": "images/13promax.jpg",
    },
    6: {
        "name": "Apple iPhone 14 (Blue, 128GB)",
        "price": 69999,
        "description": "Crash detection, great perf.",
        "image_static": "images/14r.webp",
    },
}


# Product detail page (Buy dabane ke baad)
def product_detail(request, pk):
    product = PRODUCTS.get(pk)   # <-- ab dict se data milega
    if not product:
        raise Http404("Product not found")
    return render(request, "store/checkout.html", {"product": product, "pk": pk })


# Checkout (form submit ke baad)
def checkout(request, pk):
    product = PRODUCTS.get(pk)   # <-- yaha bhi dict se data lo
    if not product:
        raise Http404("Product not found")

    if request.method == "POST":
        payment_mode = request.POST.get("payment")
        address = request.POST.get("address")

        # abhi demo ke liye sirf success page dikhayenge
        return render(request, "store/order_success.html", {
            "product": product,
            "payment": payment_mode,
            "address": address,
        })

    return redirect("product_detail", pk=pk)


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, "category_products.html", {
        "category": category,
        "products": products,
    })


def order_sucess(request):
    return render(request, "store/order_success.html", {
        
    })

# cart 
#  Store page (sab products dikhane ke liye)
def store(request):
    products = Product.objects.all()
    return render(request, "store/store.html", {"products": products})


#  Add product to cart

def add_to_cart(request, pk):
    cart = request.session.get("cart", {})

    product = PRODUCTS.get(pk)
    if not product:
        return redirect("cart")  # Agar product invalid ho toh redirect

    if str(pk) in cart:
        cart[str(pk)]["quantity"] += 1
    else:
        cart[str(pk)] = {
            "name": product["name"],
            "price": float(product["price"]),
            "description": product["description"],
            "image_static": product["image_static"],
            "quantity": 1,
        }

    request.session["cart"] = cart
    return redirect("cart")



#  Remove product from cart
def remove_from_cart(request, key):
    cart = request.session.get("cart", {})
    if key in cart:
        del cart[key]
    request.session["cart"] = cart
    return redirect("cart")




#  Cart page (sab products dikhana + total calculate karna)
def cart(request):
    cart = request.session.get("cart", {})

    for item in cart.values():
        item['total'] = item['price'] * item['quantity']

    total = sum(item["total"] for item in cart.values())

    return render(request, "store/cart.html", {"cart": cart, "total": total})


#  Single product checkout
def checkout_single(request, pk):
    product = PRODUCTS.get(pk)
    if not product:
        return redirect("cart")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("delivery")
        payment = request.POST.get("payment")

        print("Single Checkout:", name, email, address, payment, product)

        return redirect("cart")

    return render(request, "store/order.html", {"product": product})


#  Cart checkout (without pk)
def checkout_cart(request):
    cart = request.session.get("cart", {})

    for item in cart.values():
        item['total'] = item['price'] * item['quantity']

    total = sum(item["total"] for item in cart.values())

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("delivery")
        payment = request.POST.get("payment")

        print("Cart Checkout:", name, email, address, payment, cart)

        request.session["cart"] = {}  # Cart clear after checkout
        return redirect("success_cart")  # ya store page

    return render(request, "store/checkout_cart.html", {"cart": cart, "total": total})

# add to cart me checkout ke bad wla page ke liya
def success_cart(request):
    order = request.session.get('last_order', None)  # last order fetch
    return render(request, "store/order_success.html", {"order": order})
