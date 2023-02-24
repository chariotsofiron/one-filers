"""Program to find "watsky" words.

Example:
    complaint
    placement
    intention

# Instructions

$ rg "^[a-z]{9}$" words.txt > words.txt     # 9-letter words
$ sort words.txt > words.txt                # sort the words
$ python watsky_words.py words.txt          # find solutions
"""
import pathlib
import sys


def get_words(path: str) -> list[str]:
    """Reads a file into lines for the given path."""
    return pathlib.Path(path).read_text(encoding="utf-8").splitlines()


def find_words_with_prefix(words: list[str], prefix: str) -> list[str]:
    """Returns a list of words that start with the given prefix.
    Assumes that `words` is sorted and uses binary search.
    """
    # binary search for a candidate word
    left, right = 0, len(words) - 1
    while left <= right:
        mid = (left + right) // 2
        if words[mid].startswith(prefix):
            break
        if prefix < words[mid][: len(prefix)]:
            right = mid - 1
        else:
            left = mid + 1

    if left > right:
        return []

    # find neighboring solutions
    result = []
    i = mid
    while i < len(words) and words[i].startswith(prefix):
        result.append(words[i])
        i += 1

    i = mid
    while i >= 0 and words[i].startswith(prefix):
        result.append(words[i])
        i -= 1

    return result


def main() -> None:
    """Main method."""
    words = get_words(sys.argv[1])
    for first in words:
        for third in find_words_with_prefix(words, first[6:]):
            for second in find_words_with_prefix(words, first[3:6]):
                if second.endswith(third[3:6]):
                    print("---------")
                    print(first)
                    print(second)
                    print(third)


if __name__ == "__main__":
    main()
