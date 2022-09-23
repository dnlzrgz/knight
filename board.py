from config import Config
from constants import SQUARES_PER_ROW
from pathfind import Node, shortest_path
from square import Square
import random


class Board():
    def __init__(self, config: Config) -> None:
        """Initializes a 8x8 chessboard."""
        self.config = config
        self.screen = self.config.screen
        self.font = self.config.font

        self.row = range(SQUARES_PER_ROW)

        self.sq_size = self.screen.get_height() / SQUARES_PER_ROW
        self.board = [
            [Square(self.config, file, rank, self.sq_size, 1) for file in self.row] for rank in self.row]
        self.selected_square = self._select_random_square()

        self._update_board()

    def _update_board(self) -> None:
        src = self.selected_square
        src_node = Node(src.file, src.rank)

        for i, file in enumerate(self.board):
            for j, _ in enumerate(file):
                dst = self.board[i][j]
                dst_node = Node(dst.file, dst.rank)
                dst.distance = shortest_path(
                    src_node, dst_node)

    def _select_random_square(self) -> Square:
        file = random.choice(self.row)
        rank = random.choice(self.row)

        square = self.board[file][rank]
        square.distance = 0

        return square

    def draw(self) -> None:
        """Draw chessboard."""
        for file in self.board:
            for rank in file:
                rank.draw()
