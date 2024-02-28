from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):
  def setUp(self):
    self.student_1 = Student("Nik", {"Driving": ["Car", "Truck"], "Cooking": ["Pizza", "Pasta", "Cake"]})
    self.student_2 = Student("Vik", {})

  def test_initialization_with_courses(self):
    result = {"Driving": ["Car", "Truck"], "Cooking": ["Pizza", "Pasta", "Cake"]}
    self.assertEqual("Nik", self.student_1.name)
    self.assertEqual(result, self.student_1.courses)

  def test_initialization_without_courses(self):
    self.assertEqual("Vik", self.student_2.name)
    self.assertEqual({}, self.student_2.courses)

  def test_enroll_existing_course(self):
    result = self.student_1.enroll("Driving", ["Plane", "Boat"], "Y")
    self.assertEqual("Course already added. Notes have been updated.", result)
    self.assertEqual({"Driving": ["Car", "Truck", "Plane", "Boat"], "Cooking": ["Pizza", "Pasta", "Cake"]}, self.student_1.courses)

  def test_enroll_non_existing_course_with_notes_and_Y(self):
    result = self.student_2.enroll("Karate", ["Kick", "Punch"], "Y")
    self.assertEqual("Course and course notes have been added.", result)
    self.assertEqual({"Karate": ["Kick", "Punch"]}, self.student_2.courses)

  def test_enroll_non_existing_course_with_notes_and_empty_string(self):
    result = self.student_2.enroll("Karate", ["Kick", "Punch"], "")
    self.assertEqual("Course and course notes have been added.", result)
    self.assertEqual({"Karate": ["Kick", "Punch"]}, self.student_2.courses)

  def test_enroll_non_existing_course_no_notes(self):
    result = self.student_2.enroll("Sumo", ["Naked", "Fat"], "N")
    self.assertEqual("Course has been added.", result)
    self.assertEqual({"Sumo": []}, self.student_2.courses)

  def test_add_notes_existing_course(self):
    result = self.student_1.add_notes("Driving", "Skateboard")
    self.assertEqual("Notes have been updated", result)
    self.assertIn("Skateboard", self.student_1.courses["Driving"])

  def test_add_notes_non_existing_course(self):
    with self.assertRaises(Exception) as ex:
      self.student_1.add_notes("Fishing", ["Shark"])
    self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

  def test_leave_existing_course(self):
    result = self.student_1.leave_course("Driving")
    self.assertEqual("Course has been removed", result)
    self.assertTrue("Driving" not in self.student_1.courses)

  def test_leave_non_existing_course(self):
    with self.assertRaises(Exception) as ex:
      self.student_1.leave_course("Singing")
    self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
  main()