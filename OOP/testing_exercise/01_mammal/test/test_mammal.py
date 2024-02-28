from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
  name = "Um"
  type = "Dolphin"
  sound = "Onk"
  __kingdom = "animals"
  
  def setUp(self):
    self.mammal = Mammal(self.name, self.type, self.sound)

  def test_initialization(self):
    self.assertEqual(self.name, self.mammal.name)
    self.assertEqual(self.type, self.mammal.type)
    self.assertEqual(self.sound, self.mammal.sound)
    self.assertEqual(self._MammalTests__kingdom, self.mammal._Mammal__kingdom)

  def test_make_sound_returns_correct_string(self):
    result = self.mammal.make_sound()
    expected_result = f"{self.name} makes {self.sound}"
    self.assertEqual(expected_result, result)

  def test_get_kingdom_returns_correct_kingdom(self):
    result = self.mammal.get_kingdom()
    self.assertEqual(self._MammalTests__kingdom, result)
    
  def test_info_returns_correct_message(self):
    result = self.mammal.info()
    expected_result = f"{self.name} is of type {self.type}"
    self.assertEqual(expected_result, result)
    

if __name__ == "__main__":
  main()
  