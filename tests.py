import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        expected = 12.56
        self.assertEqual(expected, task.calcArea(2))

    def test4(self):
        expected = 3.14
        self.assertEqual(expected, task.calcArea(1))

    def test5(self):
        expected = ["red, blue"]
        self.assertEqual(expected, task.listEnds(["red", "green", "blue"]))

    def test6(self):
        expected = ["red, red"]
        self.assertEqual(expected, task.listEnds(["red"]))

    def test7(self):
        expected = ["red, green"]
        self.assertNotEqual(expected, task.listEnds(["red", "green", "blue"]))


if __name__ == '__main__':
    unittest.main()
