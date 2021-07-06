import unittest
from game import is_win, init_matrix


class TestWinTesting(unittest.TestCase):
    # return True or False
    def test_Win(self):
        # init matrix
        game_matrix = init_matrix()
        current_player_figure = 'X'

        # first row
        game_matrix[0][0] = current_player_figure
        game_matrix[0][1] = current_player_figure
        game_matrix[0][2] = current_player_figure
        self.assertTrue(is_win(game_matrix, current_player_figure), "First row")

        # second row
        game_matrix = init_matrix()
        game_matrix[1][0] = current_player_figure
        game_matrix[1][1] = current_player_figure
        game_matrix[1][2] = current_player_figure
        self.assertTrue(is_win(game_matrix, current_player_figure), "Second row")

        # third row
        game_matrix = init_matrix()
        game_matrix[2][0] = current_player_figure
        game_matrix[2][1] = current_player_figure
        game_matrix[2][2] = current_player_figure
        self.assertTrue(is_win(game_matrix, current_player_figure), "Third row")

        # first column
        game_matrix = init_matrix()
        game_matrix[0][0] = current_player_figure
        game_matrix[1][0] = current_player_figure
        game_matrix[2][0] = current_player_figure
        self.assertTrue(is_win(game_matrix, current_player_figure), "First column")

        # second column
        game_matrix = init_matrix()
        game_matrix[0][1] = current_player_figure
        game_matrix[1][1] = current_player_figure
        game_matrix[2][1] = current_player_figure
        self.assertTrue(is_win(game_matrix, current_player_figure), "Second column")

        # third column
        game_matrix = init_matrix()
        game_matrix[0][2] = current_player_figure
        game_matrix[1][2] = current_player_figure
        game_matrix[2][2] = current_player_figure
        self.assertTrue(is_win(game_matrix, current_player_figure), "Third column")

        # first diagonal
        game_matrix = init_matrix()
        game_matrix[0][0] = current_player_figure
        game_matrix[1][1] = current_player_figure
        game_matrix[2][2] = current_player_figure
        self.assertTrue(is_win(game_matrix, current_player_figure), "First diagonal")

        # second diagonal
        game_matrix = init_matrix()
        game_matrix[0][2] = current_player_figure
        game_matrix[1][1] = current_player_figure
        game_matrix[2][0] = current_player_figure
        self.assertTrue(is_win(game_matrix, current_player_figure), "Second diagonal")


if __name__ == '__main__':
    unittest.main()
