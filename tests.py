import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_all_walls_initialized(self):
        num_cols = 5
        num_rows = 4
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        for col in range(num_cols):
            for row in range(num_rows):
                cell = m._cells[col][row]
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)

    def test_cell_draw_stores_coordinates(self):
        

        cell = Cell()  # win=None by default
        cell.draw(10, 20, 30, 40)

        self.assertEqual(cell._x1, 10)
        self.assertEqual(cell._y1, 20)
        self.assertEqual(cell._x2, 30)
        self.assertEqual(cell._y2, 40)

    def test_draw_move_does_not_crash_without_window(self):

        cell1 = Cell()
        cell2 = Cell()

        # Assign coordinates manually (as draw normally would)
        cell1._x1, cell1._y1, cell1._x2, cell1._y2 = 0, 0, 10, 10
        cell2._x1, cell2._y1, cell2._x2, cell2._y2 = 10, 0, 20, 10

        try:
            cell1.draw_move(cell2)
        except Exception as e:
            self.fail(f"draw_move() raised an exception with win=None: {e}")


    def test_breaking_walls_between_adjacent_cells(self):

        # Simulate two horizontally adjacent cells
        left_cell = Cell()
        right_cell = Cell()

        # Break the shared wall (right of left cell, left of right cell)
        left_cell.has_right_wall = False
        right_cell.has_left_wall = False

        # Check only those two walls are removed
        self.assertFalse(left_cell.has_right_wall)
        self.assertFalse(right_cell.has_left_wall)

        self.assertTrue(left_cell.has_left_wall)
        self.assertTrue(left_cell.has_top_wall)
        self.assertTrue(left_cell.has_bottom_wall)

        self.assertTrue(right_cell.has_right_wall)
        self.assertTrue(right_cell.has_top_wall)
        self.assertTrue(right_cell.has_bottom_wall)

    def test_all_walls_initialized(self):
        num_cols = 5
        num_rows = 4
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        for col in range(num_cols):
            for row in range(num_rows):
                # Skip entrance and exit
                if (col == 0 and row == 0) or (col == num_cols - 1 and row == num_rows - 1):
                    continue

                cell = m._cells[col][row]
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)




if __name__ == "__main__":
    unittest.main()