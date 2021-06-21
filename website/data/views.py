from django.views import View
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import OrderForm, CustemerForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def Login(request):
    judul = "Halaman Login"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                messages.warning(request,'Akun Anda Belum Aktif!')

        else:
            messages.error(request,'Username dan Password Tidak Benar')
            return redirect('login')

    else:
        kontak = {
            'judul':judul,
        }
        return render(request,'auth/login.html', kontak)

def Logout(request):
    logout(request)
    messages.success(request,'Logout Berhasil')
    return redirect('login')

def Registrasi(request):
    judul = "Halaman Registrasi"
    form = SignUpForm()
    if request.method == "POST":
        formsimpan = SignUpForm(request.POST)
        if formsimpan.is_valid():
            user = formsimpan.save()

            username = formsimpan.cleaned_data.get('username')
            raw_password = formsimpan.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            messages.success(request,'Registrasi User '+ request.POST.get('username')+' Berhasil Dibuat')
            # return redirect('login')
            return HttpResponseRedirect(reverse('login'))

    kontak = {
        'judul':judul,
        'form':form,
    }

    return render(request, 'auth/registrasi.html', kontak)
    
def home(request): 
    judul = "Halaman Home"  
    
    list_custemer = Custemer.objects.all()
    list_order = Order.objects.order_by('-id')
    total_orders = list_order.count()
    delivered = list_order.filter(status= 'Delivered').count()
    pending = list_order.filter(status= 'Pending').count()

    kontak = {
        'judul':judul,
        'menu' : 'home',
        'custemer':list_custemer,
        'order': list_order,
        'data_total_orders': total_orders,
        'data_delivered': delivered,
        'data_pending':pending,
    } 
    
    return render(request, 'data/home.html', kontak)

def profil(request):
    
    return HttpResponse("<h1> Halaman Profil</h1>")

def kontak(request):
    return HttpResponse("<h1> Halaman Kontak</h1>")

def product(request):
    judul = "Halaman Product"

    list_product = Product.objects.all()

    kontak = {
        'judul':judul,
        'menu':'product',
        'dataproduct':list_product,
    }
    return render(request, 'data/product.html', kontak)
    
def custemer(request, pk):
    judul = "Halaman Custemer"
    detail_custemer = Custemer.objects.get(id=pk)
    order_custemer = detail_custemer.order_set.all()
    total_custemer = order_custemer.count()
    kontak = {
        'judul':judul,
        'menu':'custemer',
        'custemer':detail_custemer,
        'order_custemer':order_custemer,
        'total_custemer':total_custemer,
    }
    return render(request, 'data/custemer.html', kontak)
# proses CRUD
def createOrder(request):
    judul = "Halaman Create Order"
    form = OrderForm()
    if request.method == 'POST':
        formsimpan = OrderForm(request.POST)
        if formsimpan.is_valid:
             formsimpan.save()
             messages.success(request, "Order Berhasil Ditambahkan!!!")
             return redirect('/')
       
    kontak = {
        'judul':judul,
        'form':form,
    }

    # return render(request, 'data/create_order.html', kontak)
    return render(request, 'data/order_form.html', kontak)

def updateOrder(request, pk):
    judul = "Halaman Update Order"
    order = Order.objects.get(id=pk)
    formorder = OrderForm(instance=order)
    if request.method == 'POST':
        formupdate = OrderForm(request.POST, instance=order)
        if formupdate.is_valid:
            formupdate.save()
            return redirect('/')


    kontak = {
        'judul':judul,
        'form': formorder,
    }

    # return render(request, 'data/update_order.html', kontak)
    return render(request, 'data/order_form.html', kontak)
def deleteOrder(request, pk):
    judul = "Halaman Delete Order"
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request, "Order Berhasil Dihapus!!")
        return redirect('/')
     
    kontak = {
        'judul':judul,
        'form':order,
    }

    return render(request, 'data/delete_form.html', kontak)

def createCustemer(request):
    judul = "Halaman Create Custemer"
    form = CustemerForm()
    if request.method == 'POST':
        formsimpan = CustemerForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            # messages.success(request, "Custemer Berhasil Ditambahkan!!!")
            return redirect('/')

    kontak = {
        'judul':judul,
        'form':form,
    }

    return render(request, 'data/custemer_form.html', kontak)

def updateCustemer(request, pk):
    judul = "Halaman Update Custemer"
    custemer = Custemer.objects.get(id=pk)
    formcustemer = CustemerForm(instance=custemer)
    if request.method == 'POST':
        formupdate = CustemerForm(request.POST, instance=custemer)
        if formupdate.is_valid:
            formupdate.save()
            return redirect('/')

    kontak = {
        'judul':judul,
        'form':formcustemer,
    }

    return render(request, 'data/custemer_form.html', kontak)


def deleteCustemer(request, pk):
    judul = "Halaman Delete Custemer"
    custemer = Custemer.objects.get(id=pk)
    if request.method == 'POST':
        custemer.delete()
        return redirect('/')

    kontak = {
        'judul':judul,
        'form':custemer,
    }

    return render(request, 'data/delete_form.html', kontak)
