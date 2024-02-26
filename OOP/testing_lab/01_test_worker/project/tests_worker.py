from unittest import TestCase, main
from project.worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.test_worker = Worker("Koki", 1000, 100)

    def test_initialization(self):
        self.assertEqual("Koki", self.test_worker.name)
        self.assertEqual(1000, self.test_worker.salary)
        self.assertEqual(100, self.test_worker.energy)
        self.assertEqual(0, self.test_worker.money)

    def test_work_increase_money_decrease_energy(self):
        expected_energy = self.test_worker.energy - 1
        expected_money = self.test_worker.salary
        self.test_worker.work()
        self.assertEqual(expected_energy, self.test_worker.energy)
        self.assertEqual(expected_money, self.test_worker.money)

    def test_work_without_energy_raises_exception(self):
        self.test_worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.test_worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_energy_increases_when_resting(self):
        expected_energy = self.test_worker.energy + 1
        self.test_worker.rest()
        self.assertEqual(expected_energy, self.test_worker.energy)

    def test_if_get_info_returns_correct_string(self):
        expected_result = f'{self.test_worker.name} has saved {self.test_worker.money} money.'
        actual_result = self.test_worker.get_info()
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
