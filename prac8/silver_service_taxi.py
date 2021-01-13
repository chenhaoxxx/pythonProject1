

from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50  # class variable

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string of a SilverServiceTaxi."""
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get the fare."""
        return self.flagfall + super().get_fare()