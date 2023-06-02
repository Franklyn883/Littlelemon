from django.shortcuts import render,redirect
from .models import Menu
from .forms import BookingForm

#Create your views here.

def home(request):
    return render(request, 'restaurant/index.html',{})

def about(request):
    return render(request, 'about.html',{})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('restaurant:home')
    context = {'form':form}
    return render(request, 'restaurant/book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu':menu_data}
    return render(request, 'restaurant/menu.html', main_data)

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
        
    return render(request, 'restaurant/menu-item.html', {'menu_item':menu_item})
        
    
    