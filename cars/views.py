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

def car_quiz(request):
    cars = None

    if request.GET:
        cars = Car.objects.all()

        max_price = request.GET.get('max_price')
        if max_price:
            cars = cars.filter(price__lte=max_price)

        seats = request.GET.get('seats')
        if seats:
            cars = cars.filter(seats__gte=seats)

        body_type = request.GET.get('body_type')
        if body_type:
            cars = cars.filter(body_type=body_type)

        fuel_type = request.GET.get('fuel_type')
        if fuel_type:
            cars = cars.filter(fuel_type=fuel_type)

    return render(request, 'cars/car_quiz.html', {
        'cars': cars,
        'body_types': Car.BodyType.choices,
        'fuel_types': Car.FuelType.choices,
    })
def car_list(request):
    cars = Car.objects.all()

    query = request.GET.get('q')
    if query:
        cars = cars.filter(model_name__icontains=query)

    return render(request, 'cars/car_list.html', {'cars': cars, 'query': query})
