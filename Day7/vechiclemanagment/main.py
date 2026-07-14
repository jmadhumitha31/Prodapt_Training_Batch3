
from car import Car
from ev import Ev
from polymorphism import Overloading_demo
from exception import VehicleError
from report_export import export_vehicle_data


def main():
    try:
        car1 = Car("Toyota", "Camry", 2020)
        ev1 = Ev("Tesla", "Model S", 2022, 100)
        car2 = Car("Honda", "Civic", 2019)

        ev1.start_engine()
        ev1.show_info()

        car1.set_owner("Madhu")
        print(car1.get_owner())

        car2.start_engine()
        car2.show_info()

        # This may raise OwnerAlreadyExistsError
        car1.set_owner("madhunkhoidwi")

        print(car2.get_owner())

        Overloading_demo()

        vehicles = [car1, ev1, car2]
        print(export_vehicle_data("vehicle_data.csv", vehicles))

    except VehicleError as e:
        print(f"Vehicle Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()