from unittest import TestCase, main

from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.t1 = Trip(10_000.00, 1, False)
        self.t2f = Trip(10_000.00, 2, False)
        self.t2t = Trip(10_000.00, 2, True)

    def test_initialization(self):
        self.assertEqual(10_000.00, self.t1.budget)
        self.assertEqual(1, self.t1.travelers)
        self.assertFalse(False, self.t1.is_family)
        self.assertEqual({}, self.t1.booked_destinations_paid_amounts)

    def test_travelers_setter(self):
        with self.assertRaises(ValueError) as error:
            self.t1.travelers = 0
        self.assertEqual('At least one traveler is required!', str(error.exception))

    def test_family_setter(self):
        self.t1.is_family = True
        self.assertFalse(self.t1.is_family)

    def test_book_a_trip_not_valid_destination(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         self.t1.book_a_trip("Timbuktu"))

    def test_book_a_trip_not_enough_budget(self):
        self.assertEqual('Your budget is not enough!', self.t2f.book_a_trip("New Zealand"))

    def test_book_a_trip_enough_budget_not_family(self):
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 9000.00',
                         self.t2f.book_a_trip("Bulgaria"))
        self.assertEqual({"Bulgaria": 1000.00}, self.t2f.booked_destinations_paid_amounts)

    def test_book_a_trip_enough_budget_family(self):
        self.t2t.book_a_trip("Bulgaria")
        self.assertEqual({"Bulgaria": 900.00}, self.t2t.booked_destinations_paid_amounts)

    def test_booking_status_no_bookings(self):
        self.assertEqual("No bookings yet. Budget: 10000.00", self.t2f.booking_status())

    def test_booking_status_with_bookings(self):
        self.t1.book_a_trip("Bulgaria")
        self.t1.book_a_trip("Australia")
        expected = """Booked Destination: Australia
Paid Amount: 5700.00
Booked Destination: Bulgaria
Paid Amount: 500.00
Number of Travelers: 1
Budget Left: 3800.00"""
        actual = self.t1.booking_status()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
