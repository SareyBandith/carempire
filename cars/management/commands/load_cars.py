from django.core.management.base import BaseCommand
from cars.models import Brand, Car

CARS = [
    ('Toyota', 'Yaris Ascent Sport', 2024, 26000, 'hatchback', 'petrol', 5, 5.4),
    ('Toyota', 'Corolla Ascent Sport', 2024, 31000, 'hatchback', 'petrol', 5, 6.0),
    ('Toyota', 'Corolla Hybrid', 2024, 34000, 'hatchback', 'hybrid', 5, 4.0),
    ('Toyota', 'Camry Hybrid', 2024, 42000, 'sedan', 'hybrid', 5, 4.2),
    ('Toyota', 'RAV4 Hybrid', 2024, 45000, 'suv', 'hybrid', 5, 4.7),
    ('Toyota', 'Kluger Grande', 2024, 78000, 'suv', 'hybrid', 7, 5.6),
    ('Toyota', 'HiLux SR5', 2024, 63000, 'ute', 'diesel', 5, 7.9),
    ('Toyota', 'LandCruiser Prado GXL', 2024, 88000, 'suv', 'diesel', 7, 7.6),
    ('Mazda', 'Mazda 2 Pure', 2024, 25000, 'hatchback', 'petrol', 5, 5.0),
    ('Mazda', 'Mazda 3 G20 Evolve', 2024, 32000, 'hatchback', 'petrol', 5, 6.2),
    ('Mazda', 'CX-3 Touring', 2024, 33000, 'suv', 'petrol', 5, 6.3),
    ('Mazda', 'CX-5 Maxx Sport', 2024, 40000, 'suv', 'petrol', 5, 7.4),
    ('Mazda', 'CX-8 Touring', 2024, 52000, 'suv', 'diesel', 7, 6.0),
    ('Mazda', 'BT-50 XT', 2024, 48000, 'ute', 'diesel', 5, 8.0),
    ('Ford', 'Puma ST-Line', 2024, 35000, 'suv', 'petrol', 5, 5.3),
    ('Ford', 'Escape ST-Line', 2024, 42000, 'suv', 'petrol', 5, 8.6),
    ('Ford', 'Ranger XLT', 2024, 67000, 'ute', 'diesel', 5, 7.6),
    ('Ford', 'Everest Ambiente', 2024, 56000, 'suv', 'diesel', 7, 7.1),
    ('Hyundai', 'i20 N', 2024, 35000, 'hatchback', 'petrol', 5, 6.2),
    ('Hyundai', 'i30 Active', 2024, 27000, 'hatchback', 'petrol', 5, 6.5),
    ('Hyundai', 'Kona Hybrid', 2024, 38000, 'suv', 'hybrid', 5, 3.9),
    ('Hyundai', 'Tucson Elite', 2024, 40000, 'suv', 'petrol', 5, 8.1),
    ('Hyundai', 'Santa Fe', 2024, 58000, 'suv', 'diesel', 7, 6.1),
    ('Hyundai', 'Ioniq 5', 2024, 70000, 'suv', 'electric', 5, 0.0),
    ('Kia', 'Picanto S', 2024, 19000, 'hatchback', 'petrol', 5, 5.0),
    ('Kia', 'Cerato Sport', 2024, 29000, 'sedan', 'petrol', 5, 7.4),
    ('Kia', 'Seltos Sport', 2024, 33000, 'suv', 'petrol', 5, 6.9),
    ('Kia', 'Sportage SX', 2024, 38000, 'suv', 'petrol', 5, 8.1),
    ('Kia', 'Sorento GT-Line', 2024, 70000, 'suv', 'diesel', 7, 6.1),
    ('Kia', 'EV6 Air', 2024, 73000, 'suv', 'electric', 5, 0.0),
    ('Subaru', 'Impreza 2.0L', 2024, 30000, 'hatchback', 'petrol', 5, 7.2),
    ('Subaru', 'Forester 2.5i', 2024, 40000, 'suv', 'petrol', 5, 7.4),
    ('Subaru', 'Outback AWD Sport', 2024, 45000, 'wagon', 'petrol', 5, 7.3),
    ('Subaru', 'WRX AWD', 2024, 51000, 'sedan', 'petrol', 5, 9.9),
    ('Volkswagen', 'Polo Life', 2024, 30000, 'hatchback', 'petrol', 5, 5.6),
    ('Volkswagen', 'Golf 110TSI', 2024, 39000, 'hatchback', 'petrol', 5, 5.8),
    ('Volkswagen', 'Tiguan Life', 2024, 47000, 'suv', 'petrol', 5, 8.1),
    ('Volkswagen', 'Amarok Style', 2024, 72000, 'ute', 'diesel', 5, 8.4),
    ('Tesla', 'Model 3 RWD', 2024, 62000, 'sedan', 'electric', 5, 0.0),
    ('Tesla', 'Model Y RWD', 2024, 66000, 'suv', 'electric', 5, 0.0),
]


class Command(BaseCommand):
    help = "Load sample Australian car data"

    def handle(self, *args, **options):
        for brand_name, model_name, year, price, body, fuel, seats, economy in CARS:
            brand, _ = Brand.objects.get_or_create(name=brand_name)

            car, created = Car.objects.get_or_create(
                brand=brand,
                model_name=model_name,
                year=year,
                defaults={
                    'price': price,
                    'body_type': body,
                    'fuel_type': fuel,
                    'seats': seats,
                    'fuel_consumption': economy,
                },
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Added {car}"))
            else:
                self.stdout.write(f"Skipped {car}")

        self.stdout.write(self.style.SUCCESS(f"Done. {Car.objects.count()} cars in database."))