from collections import deque
from constants import SQUARES_PER_ROW, RANK, FILE


class Node():
    """Node used in BFS."""

    def __init__(self, x: int, y: int, dist=0):
        # (x, y) represent the chessboard coordinates.
        self.x = x
        self.y = y

        # minimum distance from the source.
        self.distance = dist

    def __hash__(self):
        return hash((self.x, self.y, self.distance))

    def __eq__(self, other):
        return (self.x, self.y, self.distance) == (other.x, other.y, other.distance)


def _is_valid(x: int, y: int) -> bool:
    """Check if (x, y) are valid chessboard coordinates."""
    return x >= 0 and x <= SQUARES_PER_ROW and y >= 0 and y <= SQUARES_PER_ROW


def shortest_path(src: Node, dst: Node) -> int:
    """Finds the shortest path between two squares."""

    # Check already visited nodes.
    visited = set()

    q = deque()
    q.append(src)

    while q:
        node = q.popleft()

        x = node.x
        y = node.y
        dist = node.distance

        # If destination is reached, return its distance.
        if x == dst.x and y == dst.y:
            return dist

        if node not in visited:
            visited.add(node)

            for i, _ in enumerate(RANK):
                x1 = x + RANK[i]
                y1 = y + FILE[i]

                if _is_valid(x1, y1):
                    q.append(Node(x1, y1, dist+1))

    # Return -1 if the path is not possible.
    return -1
