from config import Config
from constants import SQUARES_PER_ROW
from pathfind import Node, shortest_path
from square import Square
import random


class Board():
    def __init__(self, config: Config) -> None:
        """Initializes a 8x8 chessboard."""
        self._config = config
        self._screen = self._config.screen
        self._font = self._config.font

        self._row = range(SQUARES_PER_ROW)

        self._board = [
            [Square(self._config, file, rank, 1) for file in self._row] for rank in self._row]

        self._selected_sq = self._select_random_square()
        self._update_board()

    def _update_board(self) -> None:
        src = self._selected_sq
        src_node = Node(src.file, src.rank)

        for i, file in enumerate(self._board):
            for j, _ in enumerate(file):
                dst = self._board[i][j]
                dst_node = Node(dst.file, dst.rank)
                dst.distance = shortest_path(
                    src_node, dst_node)

    def _select_random_square(self) -> Square:
        file = random.choice(self._row)
        rank = random.choice(self._row)

        square = self._board[file][rank]
        square.distance = 0

        return square

    def reset_board_randomly(self) -> None:
        self._selected_sq = self._select_random_square()
        self._update_board()

    def draw(self) -> None:
        """Draw chessboard."""
        for file in self._board:
            for rank in file:
                rank.draw()
