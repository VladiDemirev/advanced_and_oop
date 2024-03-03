from unittest import TestCase, main
from project.robot import Robot


class RobotTests(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self):
        self.robot = Robot("Oz", "Military", 100, 1000.00)

    def test_initialization(self):
        self.assertEqual("Oz", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_invalid_category(self):
        with self.assertRaises(ValueError) as error:
            self.robot = Robot("Oz", "Home", 100, 1000.00)
        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(error.exception))

    def test_price_setter_invalid_price(self):
        with self.assertRaises(ValueError) as error:
            self.robot.price = -1
        self.assertEqual("Price cannot be negative!", str(error.exception))

    def test_upgrade_existing_hardware_component(self):
        self.robot.hardware_upgrades.append("Gun")
        result = self.robot.upgrade("Gun", 20)
        self.assertEqual(f"Robot Oz was not upgraded.", result)

    def test_upgrade_not_existing_hardware_component(self):
        result = self.robot.upgrade("Gun", 20)
        self.assertEqual(f"Robot Oz was upgraded with Gun.", result)
        self.assertEqual(["Gun"], self.robot.hardware_upgrades)
        self.assertEqual(1030, self.robot.price)

    def test_update_software_version_less_than_existing(self):
        self.robot.software_updates.append(10)
        self.robot.software_updates.append(1)
        result = self.robot.update(5.0, 50)
        self.assertEqual(f"Robot Oz was not updated.", result)

    def test_update_software_version_equal_to_existing(self):
        self.robot.software_updates = [10, 1]
        result = self.robot.update(10, 50)
        self.assertEqual(f"Robot Oz was not updated.", result)

    def test_update_capacity_less_than_needed(self):
        self.robot.software_updates.append(10)
        result = self.robot.update(15, 500)
        self.assertEqual(f"Robot Oz was not updated.", result)

    def test_update_valid_version_and_capacity(self):
        self.robot.software_updates = [10, 1]
        result = self.robot.update(15.0, 50)
        self.assertEqual(f"Robot Oz was updated to version 15.0.", result)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual([10, 1, 15.0], self.robot.software_updates)

    def test_compare_prices_of_two_robots(self):
        self.other = Robot("Iz", "Education", 120, 500.00)
        result = self.robot.__gt__(self.other)
        self.assertEqual(f"Robot with ID Oz is more expensive than Robot with ID Iz.", result)
        self.other.price = 1000
        result = self.robot.__gt__(self.other)
        self.assertEqual(f"Robot with ID Oz costs equal to Robot with ID Iz.", result)
        self.other.price = 2000
        result = self.robot.__gt__(self.other)
        self.assertEqual(f"Robot with ID Oz is cheaper than Robot with ID Iz.", result)


if __name__ == "__main__":
    main()
