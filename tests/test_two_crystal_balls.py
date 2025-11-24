import unittest

from crystalballs import two_crystal_ball_root2


class TestTwoCrystalBall(unittest.TestCase):
    def test_no_breaks(self):
        floors = [False] * 100
        self.assertEqual(two_crystal_ball_root2(floors), -1)

    def test_break_on_first_floor(self):
        floors = [True] * 100
        self.assertEqual(two_crystal_ball_root2(floors), 0)

    def test_break_on_last_floor(self):
        floors = [False] * 99 + [True]
        self.assertEqual(two_crystal_ball_root2(floors), 99)

    def test_break_on_19(self):
        floors = [False] * 19 + [True] * 81
        self.assertEqual(two_crystal_ball_root2(floors), 19)

    def test_break_on_51(self):
        floors = [False] * 51 + [True] * 81
        self.assertEqual(two_crystal_ball_root2(floors), 51)

    def test_break_on_70(self):
        floors = [False] * 70 + [True] * 81
        self.assertEqual(two_crystal_ball_root2(floors), 70)

    def test_break_on_101_out_of_105(self):
        floors = [False] * 101 + [True] * 5
        self.assertEqual(two_crystal_ball_root2(floors), 101)

    def test_empty_list(self):
        floors = []
        self.assertEqual(two_crystal_ball_root2(floors), -1)


if __name__ == "__main__":
    unittest.main()
