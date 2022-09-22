from constants import SQUARES_PER_ROW
from math import floor
from pathfind import Node, shortest_path
from square import Square
import pygame
import random


class Board():
    def __init__(self, screen: pygame.Surface, font: pygame.font) -> None:
        """Initializes a 8x8 chessboard."""
        self.screen = screen
        self.font = font

        self.row = range(SQUARES_PER_ROW)

        self.square_size = self.screen.get_height() / SQUARES_PER_ROW
        self.board = [
            [Square(self.font, file, rank, self.square_size, 1) for file in self.row] for rank in self.row]
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
                rank.draw(self.screen)
