from config import Config
from constants import SQUARES_PER_ROW
from pathfind import Node, shortest_path
from square import Square
from typing import Tuple
import random


class Board():
    def __init__(self, config: Config) -> None:
        """Initializes a 8x8 chessboard."""
        self.__config = config
        self.screen = self.__config.screen
        self.font = self.__config.font

        self.row = range(SQUARES_PER_ROW)

        self.board = [
            [Square(self.__config, file, rank, 1) for file in self.row] for rank in self.row]

        self.selected_sq = self._select_random_square()
        self._update_board()

    def _update_board(self) -> None:
        src = self.selected_sq
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

    def update_selected_sq(self, coords: Tuple) -> None:
        for i, file in enumerate(self.board):
            for j, _ in enumerate(file):
                sq = self.board[i][j]
                if sq.rect.collidepoint(coords[0], coords[1]):
                    self.selected_sq = sq
                    self._update_board()
                    return

    def reset_board_randomly(self) -> None:
        self.selected_sq = self._select_random_square()
        self._update_board()

    def draw(self) -> None:
        """Draw chessboard."""
        for file in self.board:
            for rank in file:
                rank.draw()
