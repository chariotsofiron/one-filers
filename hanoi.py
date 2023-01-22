def hanoi(n_discs: int) -> None:
    """Display solution to towers of hanoi puzzle.

    The puzzle has 3 posts indexed as 0,1,2. The discs start on post 0.

    :param n_discs: The number of discs
    """
    for i in range(1, 2**n_discs):
        print(f"move a disc from {(i & (i - 1)) % 3} to {((i | i - 1) + 1) % 3}")


if __name__ == "__main__":
    hanoi(3)
