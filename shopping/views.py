from django.shortcuts import render, redirect
from store_app.models import Product, Categories, Filter_Price, Color, Brand,Contact_us
from django.conf import settings
from django.core.mail import send_mail


def BASE(request):
    return render(request, 'main/base.html')


def HOME(request):
    product = Product.objects.filter(status='Publish')

    context = {
        'product': product,
    }
    return render(request, "main/index.html", context)


def PRODUCT(request):
    product = Product.objects.filter(status='Publish')
    # product = Product.objects.all()
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    COLORID = request.GET.get('color')
    BRANDID = request.GET.get('brand')

    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')

    PRICE_LOWTOHIGH = request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOW = request.GET.get('PRICE_HIGHTOLOW')

    NEW_PRODUCTID = request.GET.get('NEW_PRODUCT')
    OLD_PRODUCTID = request.GET.get('OLD_PRODUCT')

    # print('QQQQQQQQQQQQQQQQQQQQQQQQQQQ------------>',request.GET.get('ATOZ'))

    # print('MMMMMMMMMMMMMMMMMMMMMMM---------------->',PRICE_FILTER_ID)

    if CATID:
        product = Product.objects.filter(categories=CATID, status='Publish')
    elif PRICE_FILTER_ID:
        product = Product.objects.filter(filter_price=PRICE_FILTER_ID, status='Publish')
    elif COLORID:
        product = Product.objects.filter(color=COLORID, status='Publish')
    elif BRANDID:
        product = Product.objects.filter(brand=BRANDID, status='Publish')
    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')
    elif PRICE_LOWTOHIGH:
        product = Product.objects.filter(status='Publish').order_by('price')
    elif PRICE_HIGHTOLOW:
        product = Product.objects.filter(status='Publish').order_by('-price')
    elif NEW_PRODUCTID:
        product = Product.objects.filter(status='Publish', condition='New').order_by('-id')
    elif OLD_PRODUCTID:
        product = Product.objects.filter(status='Publish', condition='Old').order_by('-id')
    else:
        product = Product.objects.filter(status='Publish').order_by('-id')

    context = {
        'product': product,
        'categories': categories,
        'filter_price': filter_price,
        'color': color,
        'brand': brand,
    }
    return render(request, 'main/product.html', context)


def SEARCH(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains=query)

    context = {
        'product': product
    }
    return render(request, 'main/search.html', context)


def PRODUCT_DETAIL_PAGE(request, id):
    prod = Product.objects.filter(id=id).first()
    context = {
        'prod': prod
    }
    return render(request, 'main/product_single.html', context)

def Contact_Page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        
        
        subject = subject
        message = message
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from,['jiger1406@gmail.com'])
            contact.save()
            return redirect('index')
        except:
            return redirect('contact')
            
        # contact.save()
        # return redirect('index')
    
            
    return render(request, 'main/contact.html')