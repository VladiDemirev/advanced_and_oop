from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTests(TestCase):
  fuel = 50.5
  horse_power = 160.5

  def setUp(self):
    self.vehicle = Vehicle(self.fuel, self.horse_power)

  def test_initialization(self):
    self.assertEqual(self.fuel, self.vehicle.fuel)
    self.assertEqual(self.horse_power, self.vehicle.horse_power)
    self.assertEqual(self.fuel, self.vehicle.capacity)
    self.assertEqual(1.25, self.vehicle.fuel_consumption)

  def test_attributes_are_correct_instance_types(self):
    self.assertIsInstance(self.vehicle.fuel, float)
    self.assertIsInstance(self.vehicle.horse_power, float)
    self.assertIsInstance(self.vehicle.capacity, float)
    self.assertIsInstance(self.vehicle.fuel_consumption, float)
    self.assertIsInstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)

  def test_drive_when_fuel_is_enough_and_reduce_fuel(self):
    fuel_needed = 1.25 * 10
    self.fuel -= fuel_needed
    self.vehicle.drive(10)
    self.assertEqual(self.fuel, self.vehicle.fuel)
    
  def test_drive_raises_exception_when_not_enough_fuel(self):
    with self.assertRaises(Exception) as ex:
      self.vehicle.drive(100)
    self.assertEqual("Not enough fuel", str(ex.exception))

  def test_refuel_when_total_fuel_less_than_capacity_increases_fuel(self):
    self.vehicle.fuel = 40
    self.vehicle.refuel(5)
    self.assertEqual(45, self.vehicle.fuel)

  def test_refuel_raises_exception_when_too_much_fuel(self):
    with self.assertRaises(Exception) as ex:
      self.vehicle.refuel(10)
    self.assertEqual("Too much fuel", str(ex.exception))

  def test_str_returns_correct_string(self):
    result = self.vehicle.__str__()
    expected_result = f"The vehicle has {self.horse_power} " \
     f"horse power with {self.fuel} fuel left and {1.25} fuel consumption"
    self.assertEqual(expected_result, result)


if __name__ == "__main__":
  main()
    