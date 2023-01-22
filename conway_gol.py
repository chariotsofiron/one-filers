"""Conway's game of life.
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""
import itertools
from typing import Iterator

N_ROWS = 16
N_COLS = 16

Point = tuple[int, int]
State = set[Point]


def neighbours(point: Point) -> Iterator[Point]:
    """Gets the coordinates of the 8 surrounding neighbours for a point.
    Does not do range checking.
    """
    x_coord, y_coord = point
    yield x_coord + 1, y_coord
    yield x_coord - 1, y_coord
    yield x_coord, y_coord + 1
    yield x_coord, y_coord - 1
    yield x_coord + 1, y_coord + 1
    yield x_coord + 1, y_coord - 1
    yield x_coord - 1, y_coord + 1
    yield x_coord - 1, y_coord - 1


def next_state(state: State) -> State:
    """Calculates the next board state of conways game of life."""
    new_state = set()
    recalc = state | set(itertools.chain.from_iterable((neighbours(p) for p in state)))
    for point in recalc:
        count = sum((neighbour in state) for neighbour in neighbours(point))
        if count == 3 or (count == 2 and point in state):
            new_state.add(point)
    return new_state


def print_board(state: State) -> None:
    """Displays the board."""
    grid = [[" "] * N_COLS for _ in range(N_ROWS)]
    for x_coord, y_coord in state:
        grid[y_coord][x_coord] = "X"
    for row in grid:
        print("|".join(row))


def main() -> None:
    """Main method."""
    board = {(2, 2), (3, 2), (4, 2)}  # blinker
    for i in range(20):
        print(f"Iteration {i}:")
        print_board(board)
        board = next_state(board)


if __name__ == "__main__":
    main()
