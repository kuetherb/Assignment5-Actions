import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        radius = 1
        expected = math.pi
        self.assertEqual(expected, task.circle_area(radius))

    def test4(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 5]
        self.assertEqual(expected, task.list(input))

    def test5(self):
        date1 = [4, 2, 2019]
        date2 = [4, 4, 2020]
        expected = 367
        self.assertEqual(expected, task.days(date1, date2))


if __name__ == '__main__':
    unittest.main()
