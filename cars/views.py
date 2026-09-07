from django.shortcuts import render, get_object_or_404
from .models import Car


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def car_compare(request):
    ids = request.GET.getlist('cars')[:3]
    cars = Car.objects.filter(id__in=ids)
    return render(request, 'cars/car_compare.html', {'cars': cars})