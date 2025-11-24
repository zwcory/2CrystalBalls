import unittest

from crystalballs import step_counter


class TestStepCounter(unittest.TestCase):
    def test_break_on_first_floor(self):
        floors = [True] * 100
        self.assertEqual(step_counter(floors), 2)

    def test_break_on_last_floor(self):
        floors = [False] * 99 + [True]
        self.assertEqual(step_counter(floors), 20)

    def test_break_on_last_floor_10k(self):
        floors = [False] * 9999 + [True]
        self.assertEqual(step_counter(floors), 200)

    def test_break_on_last_floor_10k_less1(self):
        floors = [False] * 9998 + [True]
        self.assertEqual(step_counter(floors), 200)

    def test_break_on_last_floor_10k_less2(self):
        floors = [False] * 9997 + [True]
        self.assertEqual(step_counter(floors), 199)


if __name__ == "__main__":
    unittest.main()
