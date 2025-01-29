import unittest
from main import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    
    def test_uneven_create_cells(self):
        num_cols = 99
        num_rows = 100
        m1 = Maze(440, 400, num_rows, num_cols, 100, 100)
        self.assertNotEqual(
            len(m1._cells),
            430
        )
        self.assertNotEqual(
            len(m1._cells[1]),
            20
        )
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

if __name__ == "__main__":
    unittest.main()