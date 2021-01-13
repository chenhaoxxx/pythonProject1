

from Prac_08.taxi import Taxi


def main():
    """Test Taxi class."""
    taxi1 = Taxi("Prius 1", 100)
    taxi1.drive(40)
    print(taxi1)

    taxi1.start_fare()  # start a new fare
    taxi1.drive(100)
    print(taxi1)


if __name__ == '__main__':
    main()