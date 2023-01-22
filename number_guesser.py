"""Unwinnable Number guessing game.

# Example

```
$ python number_guesser.py
Guess a number in the range [0, 10]
> 7
Too high! Guess lower...
> 3
Too low! Guess higher...
> 4
Too low! Guess higher...
> 5
Too low! Guess higher...
You lose :(
The number I was thinking of was 6
```
"""
from random import choice
from typing import Optional


def play_game(bound: int, upper: Optional[int] = None) -> None:
    """Start an interactive number guessing game.
    [bound, upper]
    :param bound: The upper bound
    :param upper: If specified, bound becomes the lower bound and upper is the
        upper bound
    """
    if upper is None:
        lower = 0
        upper = bound
    else:
        lower = bound

    print(f"Guess a number in the range [{lower}, {upper}]")

    while upper - lower > 0:
        guess = int(input("> "))

        if (
            upper - guess > guess - lower
            # if the ranges are equal, select random partition
            or upper - guess == guess - lower
            and choice((True, False))
        ):
            lower = guess + 1
            print("Too low! Guess higher...")
        else:
            upper = guess - 1
            print("Too high! Guess lower...")

    print(f"You lose :(\nThe number I was thinking of was {upper}")


def main() -> None:
    """Main method."""
    play_game(10)


if __name__ == "__main__":
    main()
