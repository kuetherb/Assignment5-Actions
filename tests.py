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


if __name__ == '__main__':
    unittest.main()
