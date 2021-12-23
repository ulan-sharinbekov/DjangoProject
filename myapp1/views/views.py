from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from myapp1.models import Brand, Vehicle
import json
from myapp1.forms import AddVehicleForm, AddBrandForm

# Create your views here.

menu_list = ["header", "menu", "first page", "about", "footer"]

def sayHello(request):
    return render(request, 'hello.html', {"title": "Главная страница",
                                          "page": "Страница для hello",
                                          "menu_list": menu_list}
                  )

def sayH1(request):
    return render(request, 'helloh1.html', {"title": "Вторая страница",
                                            "page": "Страница для helloh1",
                                            "menu_list": menu_list
                                            }
                  )

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {
        "title": "Вторая страница",
        "cars": cars
    })

def get_brands(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {
        "title": "Вторая страница",
        "brands": brands
    })

def get_brands_by_country(request):
    brands = Brand.objects.filter(country="Germany")
    return render(request, 'brand_list.html', {
        "title": "Вторая страница",
        "brands": brands
    })

def get_vehicle_by_brand(request):
    brand = Brand.objects.get(name="Mercedes")
    cars = brand.get_vehicles.all()
    # cars = brand.vehicle_set
    return render(request, 'car_list.html', {
        "title": "Вторая страница",
        "cars": cars
    })

def get_vehicle_by_brands(request):
    cars = []
    brands = Brand.objects.filter(name__in=['Audi', 'Mercedes', 'BMW'])
    for brand in brands:
        for car in brand.get_vehicles.all():
            cars.append(car)
    print(cars)
    return render(request, 'car_list.html', {
            "title": "Вторая страница",
            "cars": cars
        })

# все машины после 2000
def get_vehicle_by_brand_after(request):
    cars = []
    cars = Vehicle.objects.filter(year__gt=2000)
    return render(request, 'car_list.html', {
        "title": "Вторая страница",
        "cars": cars
    })


# все брэнды которые начинаются на "L"
def get_vehicle_by_name_start(request):
    cars = []
    brands = Brand.objects.filter(name__startswith="L")
    return render(request, 'brand_list.html', {
        "title": "Вторая страница",
        "brands": brands
    })

# все машины сортировать по году



# все машины из Германии
def get_vehicle_by_country(request):
    cars = []
    brands = Brand.objects.filter(country__in=['Germany'])
    for brand in brands:
        for car in brand.get_vehicles.all():
            cars.append(car)
    print(cars)
    return render(request, 'car_list.html', {
            "title": "Вторая страница",
            "cars": cars
        })

def addVehicle(request):
    if request.method == 'POST':
        form = AddVehicleForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                # Vehicle.objects.create(**form.cleaned_data)
                form.save()
                return redirect('add_page')
            except:
                form.add_error(None, "Ошибка добавления")
    else:
        form = AddVehicleForm()
    return render(request, 'addVehicle.html', {'form': form})




def addBrand(request):
    if request.method == 'POST':
        form = AddBrandForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                # Vehicle.objects.create(**form.cleaned_data)
                form.save()
                return redirect('add_page')
            except:
                form.add_error(None, "Ошибка добавления")
    else:
        form = AddBrandForm()
    return render(request, 'addVehicle.html', {'form': form})