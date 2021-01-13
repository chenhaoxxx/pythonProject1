
from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Taxi F", 100, 3)
    taxi.drive(50)
    print(taxi)
    print("The total fare is $", taxi.get_fare())


main()