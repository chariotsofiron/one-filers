def hanoi(n_discs: int) -> None:
    """Prints the sequence of moves to solve the 3-pillar tower
    of hanoi puzzle with n discs starting on pillar 0.
    """
    for i in range(1, 2**n_discs):
        print(f"move a disc from {(i & (i - 1)) % 3} to {((i | i - 1) + 1) % 3}")


if __name__ == "__main__":
    hanoi(3)
