from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class SecondHandCarTests(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Panamera", "Sedan", 1000, 200_000.00)

    def test_initialization(self):
        self.assertEqual("Panamera", self.car.model)
        self.assertEqual("Sedan", self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(200_000.00, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_equal_to_1(self):
        with self.assertRaises(ValueError) as error:
            self.car.price = 1.0
        self.assertEqual('Price should be greater than 1.0!', str(error.exception))

    def test_price_setter_less_than_1(self):
        with self.assertRaises(ValueError) as error:
            self.car.price = -1
        self.assertEqual('Price should be greater than 1.0!', str(error.exception))

    def test_mileage_setter_equal_to_100(self):
        with self.assertRaises(ValueError) as error:
            self.car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(error.exception))

    def test_mileage_setter_less_than_100(self):
        with self.assertRaises(ValueError) as error:
            self.car.mileage = 50
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(error.exception))

    def test_set_promotional_price_raises_error_if_new_price_is_higher(self):
        with self.assertRaises(ValueError) as error:
            self.car.set_promotional_price(300_000)
        self.assertEqual('You are supposed to decrease the price!', str(error.exception))

    def test_set_promotional_price_new_price_is_lower(self):
        result = self.car.set_promotional_price(50_000)
        self.assertEqual('The promotional price has been successfully set.', result)
        self.assertEqual(50_000, self.car.price)

    def test_need_repair_not_acceptable_repair_price(self):
        result = self.car.need_repair(150_000, "Breaks")
        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_acceptable_repair_price(self):
        result = self.car.need_repair(10_000, "Breaks")
        self.assertEqual(f'Price has been increased due to repair charges.', result)
        self.assertEqual(210_000, self.car.price)
        self.assertIn("Breaks", self.car.repairs)

    def test_greater_than_method_overload_different_car_type(self):
        other_car = SecondHandCar("Iveco", "Truck", 500, 20_000.00)
        result = self.car.__gt__(other_car)
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_greater_than_method_overload_same_car_type(self):
        other_car_same_type = SecondHandCar("Niva", "Sedan", 1000, 2_000)
        result = self.car.__gt__(other_car_same_type)
        self.assertEqual(True, result)

    def test_str_returns_correct_string(self):
        expected = """Model Panamera | Type Sedan | Milage 1000km
Current price: 200000.00 | Number of Repairs: 0"""
        actual = self.car.__str__()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
