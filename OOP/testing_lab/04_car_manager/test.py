from unittest import TestCase, main


from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Lada", "Niva", 5, 50)

    def test_initialization(self):
        self.assertEqual("Lada", self.car.make)
        self.assertEqual("Niva", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_ivalid(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("", "Niva", 5, 50)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_setter_valid(self):
        self.assertEqual("Lada", self.car.make)

    def test_model_setter_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Lada", "", 5, 50)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_setter_valid(self):
        self.assertEqual("Niva", self.car.model)

    def test_fuel_consumption_setter_invalid_zero(self):
        with self.assertRaises(Exception) as ex:
            # self.car = Car("Lada", "Niva", 0, 50)
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_setter_invalid_minus(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Lada", "Niva", -1, 50)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_setter_valid(self):
        self.assertEqual(5, self.car.fuel_consumption)

    def test_fuel_capacity_setter_invalid_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Lada", "Niva", 5, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_invalid_minus(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Lada", "Niva", 5, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_valid(self):
        self.assertEqual(50, self.car.fuel_capacity)

    def test_fuel_amount_setter_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_setter_valid(self):
        self.assertEqual(0, self.car.fuel_amount)

    def test_refuel_invalid_amount_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_invalid_amount_minus(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_valid_amount_more_than_capacity(self):
        self.car.refuel(60)
        self.assertEqual(50, self.car.fuel_amount)

    def test_refuel_valid_amount_less_than_capacity(self):
        self.car.refuel(40)
        self.assertEqual(40, self.car.fuel_amount)

    def test_drive_invalid_distance(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_valid_distance(self):
        self.car.refuel(40)
        self.car.drive(10)
        self.assertEqual(39.5, self.car.fuel_amount)


if __name__ == "__main__":
    main()
