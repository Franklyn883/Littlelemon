from django.shortcuts import render
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
    context = {'form':form}
    return render(request, 'restaurant/book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu':menu_data}
    return render(request, 'restaurant/menu.html', main_data)